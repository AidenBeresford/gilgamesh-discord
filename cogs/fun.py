import discord
from discord.ext import commands
import random

random.seed()


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description='Rolls dice.')
    async def dice(self, ctx, sides: discord.Option(int), amount: discord.Option(int)):
        roll = 0

        for num in range(amount):
            roll += random.randrange(0, sides)

        await ctx.respond(f"D{sides} rolled {amount} time(s)! Rolled a {roll}.")


def setup(bot):
    bot.add_cog(Fun(bot))
