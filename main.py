import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default() 
intents.members = True
intents.message_content = True
rxkbot = commands.Bot(command_prefix='$', intents=intents)

@rxkbot.event
async def on_ready():
    print(f'{rxkbot.user} has connected to Discord!')

@rxkbot.command(name="rxk")
async def rxk(ctx, quote):
    filename1=open('thebible')
    wordList1=[line.rstrip('\n') for line in filename1]
    filename1.close()
    out1 = random.choice(wordList1)
    await ctx.send(f"{out1}")

rxkbot.run(TOKEN)