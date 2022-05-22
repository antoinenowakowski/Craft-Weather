import discord
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="assets/config")
client  = discord.Client()
#said : yes the bot is ready
@client.event
async def on_ready():
    print("bot ready !")


#can answer to a message who is send to the channel
@client.event
async def on_message(message):
    if message.content.lower() == 'forecast':
        await message.channel.send('When ?')
        await message.channel.send('00, 3, 6, 9, 12, 15, 18, 21 H?')
    elif message.content.lower() == '00':





#don't touch
client.run(os.getenv("TOKEN"))