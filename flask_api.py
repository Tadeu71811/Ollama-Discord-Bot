#### flask_api.py (Flask API for Llama Model)
```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Replace with your Google API key and Search Engine ID
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"

# Initialize conversation buffer for context management
conversation_buffer = []
MAX_HISTORY_LENGTH = 5  # Retain the last few exchanges

# Function to perform Google Custom Search
def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}"
    response = requests.get(url)
    if response.status_code == 200:
        items = response.json().get("items", [])
        if items:
            # Return top 3 results
            return "\n".join([f"{item['title']}: {item['link']}" for item in items[:3]])
        else:
            return "No search results found."
    return "Error: Unable to fetch search results."

@app.route('/message', methods=['POST'])
def receive_message():
    global conversation_buffer
    data = request.get_json()
    message = data.get('text', '')

    # Handle !search command
    if message.startswith("!search "):
        query = message.replace("!search ", "")
        search_results = google_search(query)
        return jsonify({'response': f"Search Results:\n{search_results}"})

    # Handle !chat command
    elif message.startswith("!chat "):
        user_message = message.replace("!chat ", "")
        conversation_buffer.append(f"User: {user_message}")
        
        # Limit buffer size for conversation history
        if len(conversation_buffer) > MAX_HISTORY_LENGTH * 2:
            conversation_buffer = conversation_buffer[-MAX_HISTORY_LENGTH * 2:]

        # Construct prompt for Ollama API with conversation history
        prompt = "\n".join(conversation_buffer)

        # Send request to Ollama API
        ollama_url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
        try:
            response = requests.post(ollama_url, json=payload)
            response.raise_for_status()
            data = response.json()
            bot_response = data.get('response', 'No valid response from Ollama.')

            # Append bot response to conversation buffer
            conversation_buffer.append(f"Bot: {bot_response}")

            return jsonify({'response': bot_response})
        except requests.RequestException as err:
            return jsonify({'response': f"Error: {err}"})

    # Default response for unrecognized commands
    return jsonify({'response': "Please use !chat to chat or !search to search the web."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
