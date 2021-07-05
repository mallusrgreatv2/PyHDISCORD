import asyncio
import random
import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord_components import Button, ButtonStyle
from random import choice
class Games(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Bot = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[  {self.__class__.__name__} Cog Loaded  ]")


    def stat(self, wonornot, botChoice):
            if wonornot == "yet":
                return "> Status: You haven't clicked any buttons"
            elif wonornot == "win":
                return f"> Status: You won! Bot chose {botChoice}!"
            elif wonornot == "out":
                return f"> Timed out! You must click on time."
            elif wonornot == "lost":
                return f"You lose! Bot chose {botChoice}"
            elif wonornot == "tie":
                return f"It's a tie! Bot chose {botChoice}"
    @commands.command(
        name = "rockpaperscissors",
        aliases = ['rps'],
        description = "Play RPS with buttons with the bot"
    )
    async def rps(self, ctx):
        stuff = ["Rock", "Paper", "Scissors"]
        comp = choice(stuff)
        name = ctx.author.display_name
        title = f"{name}'s RPS Game"
        

        yet = discord.Embed(title=title, description=self.stat("yet", comp), color=0x2e2e2e)
        win = discord.Embed(title=title, description=self.stat("win", comp), color=0x2e2e2e)
        out = discord.Embed(title=title, description=self.stat("out", comp))
        lost = discord.Embed(title=title, description=self.stat("lost", comp))
        tie = discord.Embed(title=title, description=self.stat("tie", comp))
        m = await ctx.send(
            embed=yet,
            components=[[Button(style=1, label="Rock"), Button(style=3, label="Paper"), Button(style=ButtonStyle.red, label="Scissors")]]
        )
        def check(res):
            return ctx.author == res.user and res.channel == ctx.channel
        
        try:
            res = await self.client.wait_for("button_click", check=check, timeout=15)
            player = res.component.label
            if player==comp:
                await m.edit(embed=tie,components=[])
          
            if player=="Rock" and comp=="Paper":
                await m.edit(embed=lost,components=[])
          
            if player=="Rock" and comp=="Scissors":
                await m.edit(embed=win,components=[])
        
        
            if player=="Paper" and comp=="Rock":
                await m.edit(embed=win,components=[])
          
            if player=="Paper" and comp=="Scissors":
                await m.edit(embed=lost,components=[])
          
          
            if player=="Scissors" and comp=="Rock":
                await m.edit(embed=lost,components=[])
          
            if player=="Scissors" and comp=="Paper":
                await m.edit(embed=win,components=[])
        except asyncio.TimeoutError:
            await m.edit(
                embed=out,
                components=[]
            )

    @commands.command(
        name="guess",
        description="Guess the number"
    )
    async def guess(self, ctx):
        ch = random.randint(1, 50)
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        m = await ctx.message.reply("Alright! Give me numbers between 1 and 50. I will be telling you if your number is lower than my choice or higher.")
        msgs = []
        for i in range(15):
            try:
                msg = await self.client.wait_for("message", timeout=30, check=check)
                content = int(msg.content)
                if not content:
                    await m.edit("Sure it is a number?")
                await msg.delete()
                if content == ch:
                    await m.edit("You are correct! You tried {} times and the correct number was {}".format(str(15 - i), str(ch)))
                    break
                if content <= ch:
                    await m.edit(f"Your number is lower than the bot's choice. {i+1} tries out of 15")
                if content >= ch:
                    await m.edit(f"Your number is higher than the bot's choice. {i+1} tries out of 15")
                msgs.append(msg)
            except asyncio.TimeoutError:
                await m.edit("The game timed out. You should get the correct answer within 30 seconds")

        else:
            await m.edit("Your 15 tries are over! Bot's choice was {}".format(ch))
            
    
def setup(client):
    client.add_cog(Games(client))