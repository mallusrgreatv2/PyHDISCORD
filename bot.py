# imports
from discord.ext import tasks # pip install discord.py
import discord # pip install discord.py
from discord.ext import commands # pip install discord.py
import os
import alexflipnote
from random import choice
import discord_slash # pip install discord-py-slash-command
from dotenv import load_dotenv # pip install python-dotenv
from discord_slash import SlashCommand # pip install discord-py-slash-command
# load the .env file
load_dotenv()
# statuses wee
import time

status = ['devs coding me', 'pretty funny', 'moosik!!!']
client = commands.Bot(command_prefix="??", description="made for zey nd mlsrgrt to learn dpy", owner_id=700397009336533032)
# setup slash commands
slash = SlashCommand(client, sync_commands=True)
# other stuff
client.alex = os.getenv('alex')
def alex():
    return client.alex

client.remove_command("help")
# on_ready
@client.event
async def on_ready():
    change_status.start()
    print(f"[  {client.user.name}#{client.user.discriminator} is online  ]")
    client.startTime = time.time()

# create new task that loops every 20 seconds
@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

for filename in os.listdir('cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('token'))