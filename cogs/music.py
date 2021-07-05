import discord
from discord.ext import commands, tasks
import youtube_dl
from youtubesearchpython import VideosSearch


youtube_dl.utils.bug_reports_message = lambda: ''
from utils.ytdlsource import YTDLSource
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}


from random import choice
class Music(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Bot = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[  {self.__class__.__name__} Cog Loaded  ]")

    @commands.command()
    async def play(self, ctx: commands.Context, *, song: str):
        """Play a song (currently has bugs)"""
        if not song.startswith("https://"):
            videosSearch = VideosSearch(song, limit=1)
            song = videosSearch.result()['result'][0]['link']
        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel!")
            return
        
        else:
            channel = ctx.message.author.voice.channel

        await channel.connect()
        server = ctx.message.guild
        voice_channel = server.me.voice.channel
        async with ctx.typing():
            player = await YTDLSource.from_url(song, loop=self.client.loop)
            voice_channel.play(player, after=lambda e:print('Player error: %s' % e) if e else None)
            await ctx.send("Now playing: **{}**".format(player.title))
    
    @commands.command()
    async def stop(self, ctx):
        """make bot leave your vc"""
        voice_client = ctx.message.guild.voice_client
        await voice_client.disconnect()


def setup(client):
    client.add_cog(Music(client))