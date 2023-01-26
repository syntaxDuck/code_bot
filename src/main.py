import discord
from discord.ext import commands

import os
# from dotenv import load_dotenv

#load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
GUILD = os.getenv('DISCORD_SERVER')

intents = discord.Intents().all()
# client = discord.client(intents=intents)
bot = commands.Bot(intents=intents, command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connect to Discord!')


# @client.event
# async def on_ready():
#     print(f'{client.user.name} has connect to Discord!')

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#             f'Hi {member.name}, welcome to my Discord Server!')


# @client.event
# async def on_message(message):
#     if 'time stamp' in message.content.lower():
#         time_stamp = str(datetime.now())
#         print(time_stamp)
#         await message.channel.send(time_stamp)


@bot.command(name='test', help="Does the thing")
async def test(ctx):
    await ctx.send('Hello World!')

bot.run(TOKEN)
