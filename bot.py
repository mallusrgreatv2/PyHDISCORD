import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
client = commands.Bot(command_prefix="??", description="made for zey nd mlsrgrt to learn python")

for filename in os.listdir('cogs'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('token'))