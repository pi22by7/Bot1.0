from discord.ext import commands
import discord
import asyncio

valid_users = ["ππ#0857"]


class UserMan(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member, ctx):
        joined = 0
        joined += 1
        embed = discord.Embed(title="Welcome", description=f"Have fun")
        embed.add_field(name=f"{member.mention}", value="is here :party_face:")
        await ctx.self.bot.get_channel(752932871332692088).send(content=None, embed=embed)

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if str(ctx.author) in valid_users:
            await member.kick(reason=reason)
            await ctx.send(f"{member.mention} has been kicked.")
        else:
            await ctx.send("NO")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if str(ctx.author) in valid_users:
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} begone thot")
        else:
            await ctx.send("NO")

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

    @commands.command()
    async def banlist(self, ctx):
        banned_users = await ctx.guild.bans()
        i = len(banned_users)
        if i > 0:
            while i >= 1:
                await ctx.send(banned_users)
                i -= 1
        else:
            await ctx.send("There are no banned users.")

    @commands.command()
    async def purgetest(self, ctx, amount=100):
        if str(ctx.author) in valid_users:
            for i in range(amount):
                await ctx.send("test")
            await ctx.send("done")

    @commands.Cog.listener()
    async def on_message(self, message):
        if "done" in message.content:
            await asyncio.sleep(0.2)
            await message.delete()

    @commands.command()
    async def purge(self, ctx, amount=5):
        amount = amount + 1
        if str(ctx.author) in valid_users:
            await ctx.channel.purge(limit=amount)
            if amount >= 100:
                await ctx.send(f"Purged {amount}, ordered by {ctx.message.author.mention}")
            else:
                await ctx.send("You are not allowed to use this function.")

    @commands.command()
    async def purgeall(self, ctx, channelname):
        guild = ctx.message.guild
        await self.bot.delete_channel(channelname)
        await guild.create_text_channel(channelname)

    @commands.command()
    async def useradd(self, ctx, *, arg):
        if str(ctx.author) in valid_users:
            valid_users.append(str(arg))
            await ctx.send(valid_users)
        else:
            await ctx.send("You are not allowed to use this function.")

    @commands.command()
    async def userdel(self, ctx, *, arg):
        if str(ctx.author) in valid_users:
            valid_users.remove(str(arg))
            await ctx.send(valid_users)
        else:
            await ctx.send("You are not allowed to use this function.")

    @commands.command()
    async def sudoers(self, ctx):
        if str(ctx.author) in valid_users:
            await ctx.send(valid_users)
        elif str(ctx.author) not in valid_users:
            await ctx.send("You are not allowed to use this function.")


def setup(bot):
    bot.add_cog(UserMan(bot))
