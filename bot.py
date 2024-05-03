import discord #bot controls
import requests #handling of http requests
import json #handling of json data


# GET request for a meme from the api, and the corresponding url
def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']


# configure the discord bot
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!') #get confirmation that the bot is connected to discord
        

    async def on_message(self, message):
        try:
            print(f'Message from {message.author}: {message.content}') # don't reply to own message
            if message.author == self.user:
                return

            if message.content.startswith('$hello'): #say hello
                await message.channel.send('Hello World!')
            if message.content.startswith('$meme'): # get the memes
                await message.channel.send(get_meme())
        except Exception as e: # handle errors
            print(f'Error handling message: {e}')


# select all the permissions the bot needs to read messages, reply with messages and guild (not doing that broke the code, don't ask)
intents = discord.Intents(messages = True, guilds = True, message_content = True)


client = MyClient(intents=intents) # aplly the permissions to the bot
client.run('my-token') #replace my-token with your bot token