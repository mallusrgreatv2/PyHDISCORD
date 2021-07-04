import discord
from discord.ext import commands
from discord.ext.commands import Cog, Bot
from discord_components import Button
from discord_components.component import Select, SelectOption
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
        interaction = await self.client.wait_for("button_click", check=lambda i: i.component.label.startswith("Click"))
        await interaction.channel.send("Works lol")

    @commands.command()
    async def select(self, ctx: commands.Context):
        await ctx.send('Here, select whatever you want', components = [
            Select(
                placeholder="Here!!!",
                options=[SelectOption(label="one", value="1"), SelectOption(label="two", value="2")]
            ),
            Select(
                placeholder="this is disabled lol",
                options=[SelectOption(label="hackar?", value="hacks")],
                disabled=True
            )
        ])

        interaction = await self.client.wait_for("select_option")
        await interaction.respond(content=f"{interaction.component[0].label} is it!")        

def setup(client):
    client.add_cog(Tests(client))