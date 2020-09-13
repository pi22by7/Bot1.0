from discord.ext import commands


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join", pass_context=True)
    async def join(self, ctx):
        if self.bot.user.voice:
            if self.bot.user.voice.channel.id == ctx.message.author.voice.voice_channel.id:
                await self.bot.say("I'm already in the vc.")
            else:
                await self.bot.user.voice.move_to(ctx.message.author.voice.voice_channel)  # noqa: E501
                self.bot.user.music_server = self.bot.user.voice.channel
        else:
            self.bot.user.voice = await self.bot.join_voice_channel(ctx.message.author.voice.voice_channel)  # noqa: E501
            self.bot.user.music_server = self.bot.user.voice.channel

    @commands.command()
    async def leave(self, ctx):
        await ctx.self.voice_client.disconnect()


def setup(bot):
    bot.add_cog(Music(bot))
