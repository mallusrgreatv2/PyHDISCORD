import os
import sys
import discord
from discord.ext import commands
from discord.ext.commands.core import command
class Settings(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Bot = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[  {self.__class__.__name__} Cog Loaded  ]")

    @commands.command()
    async def info(self, ctx):
        library = f"{discord.__name__}.py {discord.__version__}"
        servers = len(set(self.client.guilds))
        users = len(set(self.client.get_all_members()))
        commands = len(set(self.client.commands))
        embed = discord.Embed(title = "Information", description = f"```fix\nLibrary: {library}\nServers: {servers}\nUsers: {users}\nCommands: {commands}\n```")
        await ctx.message.reply(embed=embed)
        
def setup(c):
    c.add_cog(Settings(c))