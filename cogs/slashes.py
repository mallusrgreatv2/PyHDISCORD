import discord
from discord.ext import commands
from discord.ext.commands import cog
import discord_slash
from discord_slash import cog_ext
class Slashes(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Bot = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[  {self.__class__.__name__} Cog Loaded  ]")

    @cog_ext.cog_slash(name = "ping", guild_ids=[853316413649190912], description="Bot's latency")
    async def ping(self, ctx):
        await ctx.send("Pong! {}".format(str(round(self.client.latency))+"ms"))

    @cog_ext.cog_slash(name="say", description="say something with the bot", guild_ids=[853316413649190912])
    async def say(ctx: discord_slash.SlashContext, *, text: str):
        if '@' in text:
            await ctx.send("no")
            return
        await ctx.send(text)
    
def setup(client):
    client.add_cog(Slashes(client))