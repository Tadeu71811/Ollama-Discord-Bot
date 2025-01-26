# Ollama Discord Bot

## Overview
This bot integrates the Ollama Llama 3.2 model with Discord, enabling users to interact with the model via a chatbot. It includes:
- Google Custom Search integration for enhanced responses.
- A prompt memory feature for maintaining context.

## Features
1. **Chat Integration**: Communicate with the Llama 3.2 model.
2. **Google Custom Search**: Perform searches during conversations.
3. **Prompt Memory**: Retains up to five previous inputs for context.
4. **Flask API**: Bridges communication between Discord and Llama 3.2.

## Requirements
- Python 3.9+
- Discord.py
- Flask
- Flask-CORS
- Google Custom Search API credentials
- Ollama Llama 3.2 model hosted via Ollama

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ollama-discord-bot.git
   cd ollama-discord-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - `DISCORD_TOKEN`: Your Discord bot token.
   - `GOOGLE_API_KEY`: Your Google API key.
   - `SEARCH_ENGINE_ID`: Your Search Engine ID.

## File Structure
```
ollama-discord-bot/
├── flask_api.py      # Flask server for API requests
├── bot.py            # Discord bot logic
├── requirements.txt  # Dependencies
└── README.md         # Documentation
```

## Usage
1. Start the Flask server:
   ```bash
   python flask_api.py
   ```
2. Run the Discord bot:
   ```bash
   python bot.py
   ```
3. Interact with the bot using commands:
   - `!chat <message>`: Chat with the Llama 3.2 model.
   - `!search <query>`: Perform a Google Custom Search.
