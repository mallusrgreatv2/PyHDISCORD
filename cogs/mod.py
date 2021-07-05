import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, client) -> None:
        self: commands.Bot = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[  {self.__class__.__name__} Cog Loaded  ]")

    
    @commands.command(
        name="ban",
        description="Ban a user from server"
    )
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx: commands.Context, member: commands.MemberConverter, *, reason=None):
        guild: discord.Guild = ctx.guild
        await guild.ban(member)
        if reason is None:
            await ctx.send("Banned {}".format(member.display_name))
        else:
            await ctx.send("Banned {} for {}".format(member.display_name, reason))


def setup(client):
    client.add_cog(Mod(client))