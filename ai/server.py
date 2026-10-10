#!/usr/bin/env python3
"""Private local AI chat. Runs open-weight models through Ollama on your own machine.

You choose the model and write the system prompt, so the behavior is yours to set.
Nothing leaves your computer. Chats are saved to ai/chats/.

    ollama pull dolphin-llama3      # or any model from ollama.com/library
    python3 ai/server.py            # then open http://localhost:8800
"""
import json
import os
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
CHATS = os.path.join(HERE, "chats")
OLLAMA = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
PORT = int(os.environ.get("PORT", "8800"))
os.makedirs(CHATS, exist_ok=True)


def ollama(path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(OLLAMA + path, data=data, headers={"Content-Type": "application/json"})
    return urllib.request.urlopen(req, timeout=600)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def send_json(self, obj, code=200):
        raw = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def read_json(self):
        return json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            with open(os.path.join(HERE, "index.html"), "rb") as f:
                raw = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(raw)
        elif self.path == "/api/models":
            try:
                with ollama("/api/tags") as r:
                    self.send_json([m["name"] for m in json.load(r).get("models", [])])
            except OSError as e:
                self.send_json({"error": f"Ollama not reachable at {OLLAMA}: {e}"}, 502)
        elif self.path == "/api/chats":
            files = sorted(os.listdir(CHATS), reverse=True)
            self.send_json([f[:-5] for f in files if f.endswith(".json")])
        elif self.path.startswith("/api/chats/"):
            name = os.path.basename(self.path.split("/")[-1]) + ".json"
            try:
                with open(os.path.join(CHATS, name)) as f:
                    self.send_json(json.load(f))
            except FileNotFoundError:
                self.send_json({"error": "not found"}, 404)
        else:
            self.send_json({"error": "not found"}, 404)

    def do_POST(self):
        if self.path == "/api/save":
            body = self.read_json()
            cid = os.path.basename(body.get("id") or time.strftime("%Y%m%d-%H%M%S"))
            with open(os.path.join(CHATS, cid + ".json"), "w") as f:
                json.dump(body | {"id": cid}, f, indent=1)
            return self.send_json({"id": cid})
        if self.path != "/api/chat":
            return self.send_json({"error": "not found"}, 404)

        body = self.read_json()
        messages = [{"role": "system", "content": body.get("system", "")}] + body.get("messages", [])
        try:
            upstream = ollama("/api/chat", {
                "model": body["model"],
                "messages": messages,
                "stream": True,
                "options": {"temperature": float(body.get("temperature", 0.8))},
            })
        except OSError as e:
            return self.send_json({"error": f"Ollama error: {e}"}, 502)

        # Stream tokens straight to the browser as plain text.
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        with upstream:
            for line in upstream:
                if not line.strip():
                    continue
                chunk = json.loads(line)
                token = chunk.get("message", {}).get("content", "")
                if token:
                    self.wfile.write(token.encode())
                    self.wfile.flush()
                if chunk.get("done"):
                    break


if __name__ == "__main__":
    print(f"Local AI on http://localhost:{PORT}  (Ollama: {OLLAMA})")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
