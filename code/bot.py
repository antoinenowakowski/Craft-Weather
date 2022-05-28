import discord
import os
from dotenv import load_dotenv
from weather import get_temp, get_weather, get_clouds, get_speed_wind

liste_commands = ['forecast', 'now', '3 hours', '3', '6 hours', '6']

#token
load_dotenv(dotenv_path="assets/config")
client = discord.Client()


@client.event
async def on_ready():
    print("bot ready !")


@client.event
async def on_message(message):
    if message.content.lower() == 'forecast':
        await message.channel.send('Now ? 3 hours later ? Or 6 ?')

    # send forecast
    elif message.content.lower() == 'now':
        await message.channel.send(f'The temperature is to {get_temp(0)}\nThe weather is {get_weather(0)}, {get_clouds(0)}')
        await message.channel.send(f'The wind speed is to {get_speed_wind(0)}')
    elif message.content.lower() == '3 hours':
        await message.channel.send(f'The temperature is to {get_temp(1)}\nThe weather is {get_weather(1)}, {get_clouds(1)}')
        await message.channel.send(f'The wind speed is to {get_speed_wind(1)}')
    elif message.content.lower() == '3':
        await message.channel.send(f'The temperature is to {get_temp(1)}\nThe weather is {get_weather(1)}, {get_clouds(1)}')
        await message.channel.send(f'The wind speed is to {get_speed_wind(1)}')
    elif message.content.lower() == '6 hours':
        await message.channel.send(f'The temperature is to {get_temp(2)}\nThe weather is {get_weather(2)}, {get_clouds(2)}')
        await message.channel.send(f'The wind speed is to {get_speed_wind(2)}')
    elif message.content.lower() == '6':
        await message.channel.send(f'The temperature is to {get_temp(2)}\nThe weather is {get_weather(2)}, {get_clouds(2)}')
        await message.channel.send(f'The wind speed is to {get_speed_wind(2)}')

    # can delete message
    elif message.content.startswith("!delete"):
         number = int(message.content.split()[1])
         messages = await message.channel.history(limit=number+1).flatten()

         for each_message in messages:
              await each_message.delete()


# don't touch
client.run(os.getenv("TOKEN"))

