from discord.ext import commands
import re


class RandomE(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

        if ".hello" in message.content:
            await message.channel.send("Hi")

        elif message.content == "Wake up sheeple!":
            await message.channel.send("For ten thousand years we slumbered!")

        elif message.content == "Who's your daddy?":
            await message.channel.send(f"You :wink:")

        elif message.content == "This server is dead.":
            await message.channel.send("nope lol")

        elif message.content == "Fuck You":
            await message.channel.send("no u")

        elif message.content == "69":
            await message.channel.send('nice')

        a = re.match(r'^wp$', message.content)

        if a or message.content == "wassup" or message.content == "Wassup":
            await message.channel.send("I'm good, how are you?")


def setup(bot):
    bot.add_cog(RandomE(bot))
