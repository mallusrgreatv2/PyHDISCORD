import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord_slash import SlashCommand
load_dotenv()
client = commands.Bot(command_prefix="??", description="made for zey nd mlsrgrt to learn python")
slash = SlashCommand(client, sync_commands=True)
client.slash = slash
@slash.slash(name = "ping", guild_ids=[853316413649190912], description="Bot's latency")
async def ping(ctx):
    await ctx.send("Pong! {}".format(str(round(client.latency))+"ms"))

for filename in os.listdir('cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('token'))