# Local AI (`ai/`)

A private chat app that runs open-weight AI models on your own computer through [Ollama](https://ollama.com).
You pick the model and write the system prompt, so you set how it behaves. There's no account or API key, and nothing leaves your machine.

## Setup (about 5 minutes)

1. Install Ollama from https://ollama.com/download, then start it (`ollama serve`, or open the app).
2. Pull a model:
   - `ollama pull dolphin-llama3` (Dolphin models are tuned to follow your system prompt with minimal refusals; about 4.7 GB)
   - `ollama pull llama3.1` or `ollama pull qwen2.5` (general-purpose)
   - Any model from https://ollama.com/library works.
3. Run `python3 ai/server.py` (no pip installs needed) and open http://localhost:8800.

## Use

- **System prompt:** sets the AI's personality and rules. It's remembered between visits.
- **Temperature:** lower gives focused answers, higher gives creative ones.
- **Saved chats:** every chat saves to `ai/chats/` (git-ignored). Click one to reload it.
- **Settings:** set `PORT` to change the port and `OLLAMA_HOST` to use Ollama on another machine.

Hardware: 8 GB RAM handles 7–8B models. 16 GB or more, or a GPU, handles 13B+ models and runs faster.
