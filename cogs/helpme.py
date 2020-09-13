from discord.ext import commands
import discord


class HelpMe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def helpme(self, ctx):
        embed = discord.Embed(title="Help for Bot1.0", description="Some useful commands")
        embed.add_field(name=".helpme", value="Displays this mwssage.")
        embed.add_field(name=".hello", value="Says hey")
        embed.add_field(name=".users", value="Prints number of users (doesn't work rn, dev tried to make it universal.")
        embed.add_field(name=".join", value="Joins your VC")
        embed.add_field(name=".leave", value="Leaves the VC it was in")
        embed.add_field(name=".say", value="what?")
        embed.add_field(name=".ping", value="pong ||+ the bot client's ping to discord servers||")
        embed.add_field(name=".beep", value="Same as `.ping` but useless")
        embed.add_field(name=".wide", value="Wide")
        await ctx.channel.send(content=None, embed=embed)

    @commands.command()
    async def help_a(self, ctx):
        embed = discord.Embed(title="`sudoer's` Help for Bot1.0", description="Important commands")
        embed.add_field(name=".useradd", value="Adds specified user to trust-list. Ex: `.useradd person#tag`")
        embed.add_field(name=".userdel", value="Removes the specified user from the special-acess list.")
        embed.add_field(name=".purge", value="Purges the last `x` messages.")
        await ctx.channel.send(content=None, embed=embed)


def setup(bot):
    bot.add_cog(HelpMe(bot))
