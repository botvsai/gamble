import os
import discord
import random

from os import getenv
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv(override=True)

gamble = commands.Bot(
    command_prefix='!',
    intents=discord.Intents.all()
)

@gamble.event
async def on_ready():
    print(f'Logged in as {gamble.user}')

@gamble.command(name='gamble')
async def gamble_command(ctx):
    if random.randint(0, 100) == 42:
        await ctx.send("You won!")
    else:
        await ctx.send("You lost!")

TOKEN = getenv('DISCORD_TOKEN')

if TOKEN:
    gamble.run(TOKEN)
else:
    print("Token not found. Please set the DISCORD_TOKEN environment variable.")
