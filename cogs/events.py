import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Cog = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("---Events Cog Ready ||| Bot Ready---")

def setup(client):
    client.add_cog(Events(client))