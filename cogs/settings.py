import json
import discord
from discord.ext import commands
class Settings(commands.Cog):
    def __init__(self, client) -> None:
        self: commands.Bot = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[  {self.__class__.__name__} Cog Loaded  ]")

    @commands.command()
    async def setprefix(self, ctx, prefix: str):
        """Set custom prefix (customs are not supported yet, so the bot will stick to the default)"""
        with open('dicts/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('dicts/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        
def setup(c):
    c.add_cog(Settings(c))