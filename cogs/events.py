from inspect import signature
import discord
from discord.ext import commands
from discord_components import *
import json
from utils.prettyconcat import pretty_concat

class Events(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Bot = client

    def get_command_signature(self, command: commands.Command, ctx: commands.Context):
            aliases = "|".join(command.aliases)
            cmd_invoke = f"[{command.name}|{aliases}]" if command.aliases else command.name
            full_invoke = command.qualified_name.replace(command.name, "")

            signature = f"{ctx.prefix}{full_invoke}{cmd_invoke} {command.signature}"
            return signature

    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(self.client)
        print(f"[  {self.__class__.__name__} Cog Loaded  ]")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, commands.CommandNotFound):
            pass
        
        elif isinstance(err, commands.BadArgument):
            
            await ctx.send(f"Bad Argument. Usage:\n```{self.get_command_signature(ctx.command, ctx)}```")

        elif isinstance(err, commands.CommandOnCooldown):
            await ctx.send(f"Command is on cooldown. Retry after {err.retry_after:.2f}s")

        elif isinstance(err, commands.MissingRequiredArgument):
            missing = err.param.name
            await ctx.send(f"Missing Required Arguments. Usage:\n```{self.get_command_signature(ctx.command, ctx)}```\nMissing {missing}")
        
        elif isinstance(err, commands.BotMissingPermissions):
            permission_names = [name.replace('guild', 'server').replace('_', ' ').title() for name in err.missing_perms]
            await ctx.send('{}, I need {} permissions to run this command!'.format(
                ctx.author.mention, pretty_concat(permission_names)))
        elif isinstance(err, commands.NoPrivateMessage):
            await ctx.send(f"The command **{ctx.command}** cannot be used in private messages!")
        elif isinstance(err, commands.MissingPermissions):
            permission_names = [name.replace('guild', 'server').replace('_', ' ').title() for name in err.missing_perms]
            await ctx.send('{}, you need {} permissions to run this command!'.format(
                ctx.author.mention, pretty_concat(permission_names)))
        
        else:
            await ctx.send(f"{err.__class__.__name__}: {err}")

    async def on_guild_join(self, guild):
        with open('dicts/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = "??"

        with open('dicts/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('dicts/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('dicts/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

def setup(client):
    client.add_cog(Events(client))
