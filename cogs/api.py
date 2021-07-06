from inspect import signature
import discord
from discord.ext import commands
import alexflipnote
colors = {
    # red
    "indianred":'CD5C5C',
    "lightcoral":"F08080",
    "salmon":"FA8072",
    "darksalmon":"E9967A",
    "lightsalmon":"FFA07A",
    "crimson":"DC143C",
    "red":"ff0000",
    "firebrick":"B22222",
    "darkred":"8B0000",
    # pink
    "pink":"FFC0CB",
    "lightpink":"FFB6C1",
    "hotpink":"FF69B4",
    "deeppink":"FF1493",
    "mediumvioletred":"C71585",
    "palevioletred":"DB7093",
    # orange
    "lightsalmon":"FFA07A",
    "coral":"FF7F50",
    "tomato":"FF6347",
    "orangered":"FF4500",
    "darkorange":"FF8C00",
    "orange":"FFA500",
    # yellow
    "gold":"FFD700",
    "yellow":"ffff00",
    "lightyellow":"FFFFE0",
    "lemonchiffon":"FFFACD",
    "lightgoldenrodyellow":"FAFAD2",
    "papayawhip":"FFEFD5",
    "moccasin":"FFE4B5",
    "peachpuff":"FFDAB9",
    "palegoldenrod":"EEE8AA",
    "khaki":"F0E68C",
    "darkkhaki":"BDB76B",
    # purple
    "lavender":"E6E6FA",
    "thistle":"D8BFD8",
    "plum":"DDA0DD",
    "violet":"EE82EE",
    "orchid":"DA70D6",
    "fuchsia":"FF00FF",
    "magenta":"FF00FF",
    "mediumorchid":"BA55D3",
    "mediumpurple":"9370DB",
    "rebeccapurple":"663399",
    "blueviolet":"8A2BE2",
    "darkviolet":"9400D3",
    "darkorchid":"9932CC",
    "darkmagenta":"8B008B",
    "purple":"800080",
    "indigo":"4B0082",
    "slateblue":"6A5ACD",
    "darkslateblue":'483D8B',
    "mediumslateblue":"7B68EE",
    # green
    "greenyellow":'ADFF2F',
    "chartreuse":"7FFF00",
    "lawngreen":'7CFC00',
    "lime":"00FF00",
    "limegreen":"00FF00",
    "palegreen":"98FB98",
    "lightgreen":"90EE90",
    "mediumspringgreen":"00FA9A",
    "springgreen":"00FF7F",
    "mediumseagreen":"3CB371",
    "seagreen":"2E8B57",
    "forestgreen":"228B22",
    "green":"008000",
    "darkgreen":'006400',
    "yellowgreen":"9ACD32",
    "olivedrab":"6B8E23",
    "olive":'808000',
    "darkolivegreen":"556B2F",
    "mediumaquamarine":"66CDAA",
    "darkseagreen":"8FBC8B",
    "lightseagreen":"20B2AA",
    "darkcyan":"008B8B",
    "teal":'008080',
    # blue
    "aqua":"00FFFF",
    "cyan":"00FFFF",
    "lightcyan":"E0FFFF",
    "paleturquoise":'AFEEEE',
    "aquamarine":"7FFFD4",
    "turqtoise":"40E0D0",
    "mediumturqtoise":"48D1CC",
    "darkturqtoise":"00CED1",
    "cadetblue":"5F9EA0",
    "steelblue":'4682B4',
    "lightsteelblue":"B0C4DE",
    "powderblue":'B0E0E6',
    "lightblue":"ADD8E6",
    "skyblue":"87CEEB",
    "lightskyblue":"87CEFA",
    "deepskyblue":"00BFFF",
    "dodgerblue":"1E90FF",
    "cornflowerblue":"6495ED",
    "mediumslateblue":"7B68EE",
    "royalblue":"4169E1",
    "blue":"0000FF",
    "mediumblue":"0000CD",
    "darkblue":"00008B",
    "navy":'000080',
    "midnightblue":"191970",
    # brown
    "cornsilk":"FFF8DC",
    "blanchedalmond":"FFEBCD",
    "bisque":'FFE4C4',
    "navajowhite":'FFDEAD',
    "wheat":"F5DEB3",
    "burlywood":'DEB887',
    "tan":"D2B48C",
    "rosybrown":"BC8F8F",
    "sandybrown":"F4A460",
    "goldenrod":"DAA520",
    "darkgoldenrod":"B8860B",
    "peru":"CD853F",
    "chocolate":"D2691E",
    "saddlebrown":"8B4513",
    "sienna":"A0522D",
    "brown":"A52A2A",
    "maroon":'800000',
    "white":'FFFFFF',
    "snow":"FFFAFA",
    "honeydew":"F0FFF0",
    "mintcream":"F5FFFA",
    "azure":"F0FFFF",
    "aliceblue":"F0F8FF",
    "ghostwhite":'F8F8FF',
    "whitesmoke":"F5F5F5",
    "seashell":"FFF5EE",
    "beige":"F5F5DC",
    "oldlace":"FDF5E6",
    "floralwhite":"FFFAF0",
    "ivory":"FFFFF0",
    'antiquewhite':"FAEBD7",
    "linen":"FAF0E6",
    "lavenderblush":"FFF0F5",
    "mistyrose":"FFE4E1",
    # gray
    "gainsboro":"DCDCDC",
    "lightgray":"D3D3D3",
    "silver":"C0C0C0",
    "darkgray":"A9A9A9",
    "gray":"808080",
    "dimgray":"696969",
    "lightslategray":"778899",
    "slategray": '708090',
    "darkslategray":"2F4F4F",
    "black":"000000"
}
class API(commands.Cog):
    def __init__(self, client) -> None:
        self.client: commands.Bot = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[  {self.__class__.__name__} Cog Loaded  ]")

    async def get_api(self):
        return alexflipnote.Client(token=self.client.alex)

    def api(self):
        return self.get_api()

    @commands.command(
        name="amiajoke",
        aliases=['joke', 'aiaj', 'amia'],
        description="Am I a Joke to you?!?!?"
    )
    async def amiajoke(self, ctx: commands.Context, author: commands.UserConverter = None):
        author: discord.User = author or ctx.author
        avatar = author.avatar_url_as(format="png", size=4096)
        m = await ctx.message.reply(content="Rendering...", mention_author=False)
        client = await self.api()
        embed = discord.Embed(title = f"Rendered by {ctx.author.name}").set_image(url="attachment://amiajoke.png")
        img = discord.File(await (await client.amiajoke(image=avatar)).read(), "amiajoke.png")
        await ctx.message.reply(embed=embed, file=img, mention_author=False)
        await m.edit(content="Rendered!")

    @commands.command(
        name="supreme",
        description="brrrrr"
    )
    async def supreme(self, ctx, *, text: str):
        m = await ctx.message.reply(content="Rendering...", mention_author=False)
        client = await self.api()
        embed = discord.Embed(title = f"Rendered by {ctx.author.name}").set_image(url="attachment://supreme.png")
        img = discord.File(await (await client.supreme(text=text)).read(), "supreme.png")
        await ctx.message.reply(embed=embed, file=img, mention_author=False)
        await m.edit(content="Rendered!")

    @commands.command(
        name="bad",
        description="everyone is bad at something"
    )
    async def bad(self, ctx: commands.Context, author: commands.UserConverter = None):
        author: discord.User = author or ctx.author
        avatar = author.avatar_url_as(format="png", size=4096)
        m = await ctx.message.reply(content="Rendering...", mention_author=False)
        client = await self.get_api()
        embed = discord.Embed(title = f"Rendered by {ctx.author.name}").set_image(url="attachment://bad.png")
        img = discord.File(await (await client.bad(image=avatar)).read(), "bad.png")
        await ctx.message.reply(embed=embed, file=img, mention_author=False)
        await m.edit(content="Rendered!")

    @commands.command(
        name="calling",
        description="tom and jerry",
        aliases = ['call']
    )
    async def calling(self, ctx, *, text: str):
        m = await ctx.message.reply(content="Rendering...", mention_author=False)
        client = await self.api()
        embed = discord.Embed(title = f"Rendered by {ctx.author.name}").set_image(url="attachment://calling.png")
        img = discord.File(await (await client.calling(text=text)).read(), "calling.png")
        await ctx.message.reply(embed=embed, file=img, mention_author=False)
        await m.edit(content="Rendered!")

    @commands.command(
        name="captcha",
        description="~~fake~~ captcha",
        aliases = ['capt']
    )
    async def captcha(self, ctx, *, text: str):
        m = await ctx.message.reply(content="Rendering...", mention_author=False)
        client = await self.api()
        embed = discord.Embed(title = f"Rendered by {ctx.author.name}").set_image(url="attachment://captcha.png")
        img = discord.File(await (await client.captcha(text=text)).read(), "captcha.png")
        await ctx.message.reply(embed=embed, file=img, mention_author=False)
        await m.edit(content="Rendered!")

    @commands.command(
        name="achievement",
        description="~~fake~~ achievement",
        aliases = ['achieve']
    )
    async def achievement(self, ctx, *, text: str):
        m = await ctx.message.reply(content="Rendering...", mention_author=False)
        client = await self.api()
        embed = discord.Embed(title = f"Rendered by {ctx.author.name}").set_image(url="attachment://achievement.png")
        img = discord.File(await (await client.achievement(text=text)).read(), "achievement.png")
        await ctx.message.reply(embed=embed, file=img, mention_author=False)
        await m.edit(content="Rendered!")

    @commands.command(
        name="colorify",
        description="color someones avatar",
        aliases = ['colourify']
    )
    async def color(self, ctx, clr: str, user: commands.UserConverter = None):
        if not colors[clr]:
            await ctx.message.reply(f"Color {clr} not found.")
            return
        user = user or ctx.author
        client = await self.api()
        avatar = user.avatar_url_as(format="png", size=4096)
        img = discord.File(await (await client.colourify(image=avatar, colour=colors[clr])).read(), "colorify.png")
        embed = discord.Embed(title = f"Rendered by {ctx.author.name}").set_image(url="attachment://colorify.png")
        await ctx.message.reply(embed=embed, file=img)


def setup(client):
    client.add_cog(API(client))