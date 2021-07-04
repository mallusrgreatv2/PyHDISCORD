import discord
from discord.ext import commands
from discord_components import *
class Events(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Bot = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("---Events Cog Ready ||| Bot Ready---")
        DiscordComponents(self.client)
        await self.client.change_presence(activity=discord.Game("games"))

def setup(client):
    client.add_cog(Events(client))