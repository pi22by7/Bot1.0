from discord.ext import commands
import asyncio


class FunC(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wide(self, ctx):
        await ctx.send("https://tenor.com/view/wide-putin-walk-wide-screen-expanded-gif-17474729")

    @commands.Cog.listener()
    async def on_message(self, message):
        if ".wide" in message.content:
            await asyncio.sleep(0.2)
            await message.delete()

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def beep(self, ctx):
        await ctx.send("boop")

    @commands.command()
    async def say(self, ctx, *, arg):
        await ctx.send(arg)


def setup(bot):
    bot.add_cog(FunC(bot))
