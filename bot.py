# imports
from discord.ext import tasks
import discord
from discord.ext import commands
import os
from random import choice
from dotenv import load_dotenv
from discord_slash import SlashCommand
import json
# load the .env file
load_dotenv()
# statuses wee

status = ['devs coding me', 'pretty funny', 'moosik!!!']
def get_prefix(client, message):
    with open('dicts/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix="??", description="made for zey nd mlsrgrt to learn dpy")
# setup slash commands
slash = SlashCommand(client, sync_commands=True)
client.slash = slash
# ping slash cmd
# @slash.slash(name = "ping", guild_ids=[853316413649190912], description="Bot's latency")
# async def ping(ctx):
#     await ctx.send("Pong! {}".format(str(round(client.latency))+"ms"))
client.remove_command("help")

# on_ready
@client.event
async def on_ready():
    change_status.start()
    print(f"[  {client.user.name}#{client.user.discriminator} is online  ]")

# create new task that loops every 20 seconds
@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

for filename in os.listdir('cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('token'))