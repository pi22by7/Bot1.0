from discord.ext import commands
import time
import asyncio


class Logger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def update_stats(self):
        messages = 0
        joined = 0
        messages += 1

        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            try:
                with open("stats.txt", "a") as f:
                    f.write(f"Time: {time.time()}, Messages: {messages}, Members Joined: {joined}\n")

                await asyncio.sleep(10)
            except Exception as e:
                print(e)
                await asyncio.sleep(10)
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(Logger(bot))
