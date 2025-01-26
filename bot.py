#### bot.py (Discord Bot Logic)
```python
import discord
from discord.ext import commands
import requests
import uuid  # For generating unique request IDs

# Insert your actual Discord bot token here
TOKEN = 'your_token_here'

# Configure bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user.name}")

# Function to split long messages for Discord
def split_message(message, max_length=2000):
    return [message[i:i + max_length] for i in range(0, len(message), max_length)]

# Chat command to send a message to Flask for processing
@bot.command(name='chat')
async def chat(ctx, *, message):
    api_url = "http://localhost:5000/message"
    unique_id = str(uuid.uuid4())  # Generate unique ID for each request

    try:
        # Send message to the Flask API
        response = requests.post(api_url, json={'text': f"!chat {message}", 'unique_id': unique_id})
        response.raise_for_status()  # Raise an error for 4XX/5XX responses
        data = response.json()
        
        # Retrieve and send the response back in parts to avoid character limits
        response_text = data.get('response', 'No response from API')
        for part in split_message(response_text):
            await ctx.send(part)
    except requests.RequestException as e:
        await ctx.send(f"Error connecting to API: {e}")
    except ValueError:
        await ctx.send("Error: Unable to parse API response as JSON")

# Search command to trigger a search request
@bot.command(name='search')
async def search(ctx, *, query):
    api_url = "http://localhost:5000/message"
    unique_id = str(uuid.uuid4())  # Generate unique ID for each request

    try:
        # Send search query to the Flask API
        response = requests.post(api_url, json={'text': f"!search {query}", 'unique_id': unique_id})
        response.raise_for_status()  # Raise an error for 4XX/5XX responses
        data = response.json()
        
        # Retrieve and send the response back in parts to avoid character limits
        response_text = data.get('response', 'No response from API')
        for part in split_message(response_text):
            await ctx.send(part)
    except requests.RequestException as e:
        await ctx.send(f"Error connecting to API: {e}")
    except ValueError:
        await ctx.send("Error: Unable to parse API response as JSON")
