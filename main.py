import os
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='.')
owner = ["ππ#0857"]


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded cogs.{extension}")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded cogs.{extension}")


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Refreshed cogs.{extension}")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.command()
async def logoff(ctx):
    if str(ctx.author) in owner:
        await ctx.send("Shutting down the bot. \n\n"
                       "The reasons can be various: \n"
                       "Most likely I might be having a maintenance break. \n"
                       "I will resume normal services ASAP. ")
        await asyncio.sleep(0.5)
        return await bot.logout()
    else:
        await ctx.send("Only the bot owner can log me out.")


bot.run("NzMxNDEyMjcyNTA0NjM1NDIy.Xwn9fQ.7301GsfLSn_0DxMyRxmTIFmqBQo")
