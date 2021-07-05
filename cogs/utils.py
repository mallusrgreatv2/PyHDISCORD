from discord.ext.commands.cooldowns import BucketType
from utils.paginator import Pag
import discord
from discord.ext import commands
from pistonapi import PistonAPI
from datetime import datetime
import a,asyncio,os
from discord import Embed,Color
versions={"javascript":"15.10.0"
 , "python":"3.9","bash":"5.1.0",'brainfuck':'2.7.3','cjam':'0.6.5','clojure':'1.10.3','cobol':'3.1.2','coffeescript':'2.5.1',
  'cow':'1.0.0','crystal':'0.36.1','dart':'2.12.1','dash':'0.5.11','deno':'1.7.5','dotnet':'5.0.201','dragon':'1.9.8',
  'elixir':'1.11.3','emacs':'27.1.0','erlang':'23.0.0','gawk':'5.1.0','gcc':'10.2.0','go':'1.16.2','golfscript':'1.0.0',
  'groovy':'3.0.7','haskell':'9.0.1','java':'15.0.2','jelly':'0.1.31','kotlin':'1.4.31','lisp':'2.1.2','lolcode':'0.11.2',
  'lua':'5.4.2','mono':'6.12.0','nasm':'2.15.5','nim':'1.4.4','node':'16.3.0','ocaml':'4.12.0','octave':'6.2.0',
  'osabie':'1.0.1','paradoc':'0.6.0','pascal':'3.2.0','perl':'5.26.1','php':'8.0.2','ponylang':'0.39.0','prolog':'8.2.4',
  'pure':'0.68.0','pyth':'1.0.0','raku':'6.100.0','rockstar':'1.0.0','rust':'1.50.0','scala':'3.0.0','swift':'5.3.3',
  'typescript':'4.2.3','vlang':'0.1.13','yeethon':'3.10.0','ruby':'3.0.1',"julia":"1.6.1"
  }

piston = PistonAPI()

class Utils(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Bot = client
        self.cmds_per_page = 10
    
    def get_command_signature(self, command: commands.Command, ctx: commands.Context):
        aliases = "|".join(command.aliases)
        cmd_invoke = f"[{command.name}|{aliases}]" if command.aliases else command.name
        full_invoke = command.qualified_name.replace(command.name, "")

        signature = f"{ctx.prefix}{full_invoke}{cmd_invoke} {command.signature}"
        return signature

    async def return_filtered_commands(self, walkable, ctx):
        filtered = []

        for c in walkable.walk_commands():
            try:
                if c.hidden:
                    continue
                elif c.parent:
                    continue
                await c.can_run(ctx)
                filtered.append(c)
            except commands.CommandError:
                continue
        
        return self.return_sorted_commands(filtered)

    def return_sorted_commands(self, commandList):
        return sorted(commandList, key=lambda x: x.name)

    async def setup_help_pag(self, ctx, entity=None, title=None):
        entity = entity or self.client
        title = title or self.client.description

        pages = []

        if isinstance(entity, commands.Command):
            filtered_commands = (
                list(set(entity.all_commands.values()))
                if hasattr(entity, "all_commands")
                else []
            )
            filtered_commands.insert(0, entity)

        else:
            filtered_commands = await self.return_filtered_commands(entity, ctx)

        for i in range(0, len(filtered_commands), self.cmds_per_page):
            next_commands = filtered_commands[i : i + self.cmds_per_page]
            commands_entry = ""

            for cmd in next_commands:
                desc = cmd.short_doc or cmd.description
                signature = self.get_command_signature(cmd, ctx)
                subcommand = "[subcommands_supported]" if hasattr(cmd, "all_commands") else ""

                commands_entry += (
                    f"**{cmd.name}**\n```\n{signature}\n```\n{desc}"
                    if isinstance(entity, commands.Command)
                    else f"**{cmd.name}**\n{desc}\n    {subcommand}"
                )
            pages.append(commands_entry)

        await Pag(title=title, color=0xCE2029, entries=pages, length=1).start(ctx)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[  {self.__class__.__name__} Cog Loaded  ]")
    
    @commands.cooldown(rate=1, per=3,type=BucketType.user)
    @commands.command(
        name="help", aliases=["h", "commands"], description="The help command!"
    )
    
    async def help_command(self, ctx, *, cogOrCommand=None):
        """
        All the commands or cog commands or command information
        """
        if not cogOrCommand:
            await self.setup_help_pag(ctx, title="PyH")

        else:
            cog = self.client.get_cog(cogOrCommand)
            if cog:
                await self.setup_help_pag(ctx, cog, f"{cog.qualified_name}'s commands")

            else:
                command = self.client.get_command(cogOrCommand)
                if command:
                    await self.setup_help_pag(ctx, command, command.name)

                else:
                    await ctx.send("Entity not found.")

    @commands.command(
        name="code",
        description="run code in different languages",
        aliases=['run']
    )
    async def code(self, ctx: commands.Context, language: str="python", *, code: str="print(\"Why didn't u put any codes?!\")"):
        msg= await ctx.send("Executing...")
        try:
            #await asyncio.sleep(0.33)
            language = language.lower()
            version = versions[language]
            code = code.replace("```","")
        # await msg.edit(embed=load[1])
        # await asyncio.sleep(0.33)
            start = datetime.now()
            output =str(piston.execute(language=language, version=version,code=code))
            taken = datetime.now() - start #taken =  taken.total_secs()*1000
            taken = str(taken)
            taken = taken.replace("0:00:",'')
            #await msg.edit(embed=load[2])
            #await asyncio.sleep(0.33)
            if "/piston/" in output and "file0.code" in output:
                output =  output.replace('file0.code:','lol.html:in Line ')
                em = Embed(title="Critical Error", description=f"{output}",color=Color.red())
            
                em.set_footer(text=f"Time Taken: {taken} s")
            # await msg.edit(embed=load[0])
            # await asyncio.sleep(0.1)
            # await msg.edit(embed=load[1])
            # await msg.edit(embed=load[2])
                await msg.edit(embed=em)
                await msg.add_reaction("❌")
            
            else:
                em = Embed(title="Code Output:", description=f"{output}",color=0x00ff00)
            
                em.set_footer(text=f'{language} v{version} || Time Taken : {taken} s')
                await msg.edit(embed=em)
                await msg.add_reaction("✅")
        except Exception as e:
            await msg.edit(embed=Embed(title="Error", description=f"{e}"))
        

                    
def setup(client):
    client.add_cog(Utils(client))
