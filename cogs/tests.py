import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord_components import Button
class Tests(Cog):
    def __init__(self, client) -> None:
        self.client: Cog = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("[  Tests Cog Loaded  ]")

    @commands.command()
    async def button(self, ctx: commands.Context):
        await ctx.send("Here is your button", components= [
            Button(label="Click", style = 1),
            Button(label="Disabled", disabled=True)
        ])
        interaction = await self.client.wait_for("button_click", check=lambda i: i.component.label == 'Click')
        interaction.reply("hey")


def setup(client):
    client.add_cog(Tests(client))