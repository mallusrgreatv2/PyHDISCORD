import discord
from discord.ext import commands
from discord_components import *
class Events(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Bot = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[  {self.client.user.name}#{self.client.user.discriminator} is online  ]")
        DiscordComponents(self.client)
        await self.client.change_presence(activity=discord.Game("games"))
        print(f"[  {self.__class__.__name__} Cog Loaded  ]")

def setup(client):
    client.add_cog(Events(client))