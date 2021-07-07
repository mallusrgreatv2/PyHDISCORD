import discord
from discord.ext import commands
import io
import textwrap
from contextlib import redirect_stdout
import traceback
class Owner(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Bot = client
        self.bot: commands.Bot = client

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    @commands.command(pass_context=True, hidden=True, name='eval')
    @commands.is_owner()
    async def _eval(self, ctx, *, body: str):
        """Evaluates a code"""

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                await ctx.send(f'```py\n{value}{ret}\n```')

    @commands.group(name="cogs", hidden=True, invoke_without_command=True)
    @commands.is_owner()
    async def _cogs(self, ctx):
        await ctx.message.reply("reload, load, unload")

    @_cogs.command(name="reload")
    @commands.is_owner()
    async def _reload(self, ctx, extension):
        self.client.reload_extension(extension)
        await ctx.message.reply("Reloaded", mention_author=False)

    @_cogs.command(name="load")
    @commands.is_owner()
    async def _load(self, ctx, extension):
        self.client.load_extension(extension)
        await ctx.message.reply("Loaded", mention_author=False)

    @_cogs.command(name="unload")
    @commands.is_owner()
    async def _unload(self, ctx, extension):
        self.client.unload_extension(extension)
        await ctx.message.reply("Unloaded", mention_author=False)


def setup(client):
    client.add_cog(Owner(client))