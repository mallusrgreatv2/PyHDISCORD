import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Bot = client

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

    @commands.command(
        name="kick",
        description="Kick a user from server"
    )
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx: commands.Context, member: commands.MemberConverter, *, reason = None):
        guild: discord.Guild = ctx.guild
        await guild.kick(member)
        if reason is None:
            await ctx.send("Kicked {}".format(member.display_name))
        else:
            await ctx.send("Kicked {} for {}".format(member.display_name, reason))

    @commands.command(
        name="purge",
        aliases = ['clean', 'clear'],
        description="Purge x amount of messages. types:\n`members: purge all of the non-bots' messages`\n`bots: purge all of the bots' messages`\n`my: purge all of PyH's messages`\n`pinned: purge all pinned messages`\nif none are given, bot won't do any checks"
    )
    async def purge(self, ctx: commands.Context, number: int, type = None):
        def pinned_check(message: discord.Message):
            return message.pinned

        def bots_check(message: discord.Message):
            ch: discord.TextChannel = message.channel
            return message.author.bot == True

        def members_check(message: discord.Message):
            ch: discord.TextChannel = message.channel
            return message.author.bot == False
        
        def my_check(message: discord.Message):
            return message.author == self.client.user
        
        channel: discord.TextChannel = ctx.channel
        if not type:
            await channel.purge(limit=number)
        elif type == 'pinned':
            await channel.purge(limit=number, check=pinned_check)
        elif type == 'bots':
            await channel.purge(limit=number, check=bots_check)
        elif type == 'members':
            await channel.purge(limit=number, check=members_check)
        elif type == 'my':
            await channel.purge(limit=number, check=my_check)
        else:
            await ctx.message.reply("Invalid command. Choose one of these: `pinned, bots, members, my`")

    @commands.command(
        name = "role"
    )
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def role(self, ctx, member: commands.MemberConverter, role: commands.RoleConverter):
        member: discord.Member = member
        for i in member.roles:
            if role.id == i.id:
                await member.remove_roles(role)
                await ctx.message.reply(f"Removed {role.name} from {member.display_name}")
                break
        else:
            await member.add_roles(role)
            await ctx.message.reply(f"Gave {role.name} to {member.display_name}")


def setup(client):
    client.add_cog(Mod(client))