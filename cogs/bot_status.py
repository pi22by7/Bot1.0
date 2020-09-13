import discord
from discord.ext import commands


class BotStatus(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("I'm alive.")
        print("Logged in as: ", self.bot.user)
        print("ID: ", self.bot.user.id)
        print(discord.__version__)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                                 name="for .helpme to serve you!"))

    @commands.command()
    async def discordpy_version(self, ctx):
        await ctx.send(discord.__version__)

    @commands.command()
    async def dbot_version(self, ctx):
        await ctx.send("The Bot Version is: `0.40b`")


def setup(bot):
    bot.add_cog(BotStatus(bot))
