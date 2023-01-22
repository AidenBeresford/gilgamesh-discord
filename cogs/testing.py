import discord
from discord.ext import commands


class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def ping(self, ctx):
        await ctx.respond("Pong!")


def setup(bot):
    bot.add_cog(Testing(bot))
