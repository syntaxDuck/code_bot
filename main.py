import discord
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
GUILD = os.getenv('DISCORD_SERVER')

intents = discord.Intents().all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connect to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord Server!')


@client.event
async def on_message(message):
    if 'time stamp' in message.content.lower():
        time_stamp = str(datetime.now())
        print(time_stamp)
        await message.channel.send(time_stamp)

client.run(TOKEN)
