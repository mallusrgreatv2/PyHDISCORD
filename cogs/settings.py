from discord.ext import commands
class Settings(commands.Cog):
    def __init__(self, client) -> None:
        self: commands.Bot = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[  {self.__class__.__name__} Cog Loaded  ]")

        
def setup(c):
    c.add_cog(Settings(c))