import discord
import re
import time
import asyncio
from discord.ext import commands

# from discord.ext.commands import Bot
# from discord.utils import get
# import youtube_dl



@bot.command()
async def getguild(ctx):
    gid = ctx.message.guild.id
    return gid


@bot.command()
async def guid():
    userno = getguild.member_count
    return userno

# log


async def update_stats():
    messages = 0
    joined = 0
    messages += 1

    await bot.wait_until_ready()

    while not bot.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {time.time()}, Messages: {messages}, Members Joined: {joined}\n")

            await asyncio.sleep(10)
        except Exception as e:
            print(e)
            await asyncio.sleep(10)
    await bot.wait_until_ready()


# random commands (basic)




@bot.command()
async def users(ctx):
    await ctx.send(len(ctx.guild.members))  # includes bots




# welcome message


@bot.event


# voice channel







# chat manipulation


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if str(ctx.author) in valid_users:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked.")
    else:
        await ctx.send("NO")


@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if str(ctx.author) in valid_users:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} begone thot")
    else:
        await ctx.send("NO")


@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


@bot.command()
async def banlist(ctx):
    banned_users = await ctx.guild.bans()
    i = len(banned_users)
    if i > 0:
        while i >= 1:
            await ctx.send(banned_users)
            i -= 1
    else:
        await ctx.send("There are no banned users.")


@bot.command()
async def purge(ctx, amount=5):
    amount = amount + 1
    if str(ctx.author) in valid_users:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send("You are not allowed to use this function.")


@bot.command()
async def useradd(ctx, arg):
    if str(ctx.author) in valid_users:
        valid_users.append(str(arg))
        await ctx.send(valid_users)
    else:
        await ctx.send("You are not allowed to use this function.")


@bot.command()
async def userdel(ctx, arg):
    if str(ctx.author) in valid_users:
        valid_users.remove(str(arg))
        await ctx.send(valid_users)
    else:
        await ctx.send("You are not allowed to use this function.")


@bot.command()
async def sudoers(ctx):
    if str(ctx.author) in valid_users:
        await ctx.send(valid_users)
    elif str(ctx.author) not in valid_users:
        await ctx.send("You are not allowed to use this function.")


@bot.command()
async def helpme(ctx):
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


@bot.command()
async def help_a(ctx):

    embed = discord.Embed(title="`sudoer's` Help for Bot1.0", description="Important commands")
    embed.add_field(name=".useradd", value="Adds specified user to trust-list. Ex: `.useradd person#tag`")
    embed.add_field(name=".userdel", value="Removes the specified user from the special-acess list.")
    embed.add_field(name=".purge", value="Purges the last `x` messages.")
    await ctx.channel.send(content=None, embed=embed)


bot.loop.create_task(update_stats())
# bot.run("NzMxNDEyMjcyNTA0NjM1NDIy.Xwn9fQ.7301GsfLSn_0DxMyRxmTIFmqBQo")
