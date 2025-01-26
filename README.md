# Ollama-Discord-Bot
Turning your locally hosted Ollama model into a discord bot. 
# Ollama Discord Bot

## Overview
This bot integrates the Ollama Llama 3.2 model with Discord, enabling users to interact with the model via a chatbot. It includes Google Custom Search integration for enhanced responses and a prompt memory feature for maintaining context in conversations.

## Features
1. **Chat Integration**: Interactive communication with the Llama 3.2 model.
2. **Google Custom Search**: Provides additional search capabilities during conversations.
3. **Prompt Memory**: Remembers up to five previous user inputs to maintain context.
4. **Flask API**: Facilitates communication between Discord and the Llama 3.2 backend.

---

### Requirements
- Python 3.9+
- Discord.py
- Flask
- Flask-CORS
- Google Custom Search API credentials
- Ollama Llama 3.2 model hosted via Ollama

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ollama-discord-bot.git
   cd ollama-discord-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add environment variables:
   - `DISCORD_TOKEN`: Your Discord bot token.
   - `GOOGLE_API_KEY`: Your Google Custom Search API key.
   - `SEARCH_ENGINE_ID`: Your Google Custom Search engine ID.

---

### File Structure
```
ollama-discord-bot/
├── flask_api.py      # Flask server for handling API requests
├── bot.py            # Discord bot logic
├── requirements.txt  # Dependencies
└── README.md         # Project documentation

### Usage
1. Start the Flask server:
   ```bash
   python flask_api.py
   ```
2. Run the Discord bot:
   ```bash
   python bot.py
   ```
3. Interact with the bot in your Discord server.

---

### Recommendations
If the project grows further, consider splitting the `flask_api.py` and `bot.py` into modules to improve maintainability. For instance:
- Keep API routes and logic modular.
- Manage configurations (like API keys and tokens) using environment variables or a dedicated configuration file.
