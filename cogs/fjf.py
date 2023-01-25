import random
import discord
from discord.ext import commands

wind_jobs = ('knight', 'monk', 'thief', 'white mage', 'black mage', 'blue mage')
water_jobs = ('red mage', 'time mage', 'summoner', 'berserker', 'mystic knight')
fire_jobs = ('ninja', 'hunter', 'geomancer', 'beastmaster', 'bard')
earth_jobs = ('dragoon', 'samurai', 'dancer', 'chemist')

random.seed()


class FJF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def wind(self, ctx):
        await ctx.respond('Wind: ' + wind_jobs[random.randrange(0, len(wind_jobs))].title())

    @discord.slash_command()
    async def water(self, ctx):
        await ctx.respond('Water: ' + water_jobs[random.randrange(0, len(water_jobs))].title())

    @discord.slash_command()
    async def fire(self, ctx):
        await ctx.respond('Fire: ' + fire_jobs[random.randrange(0, len(fire_jobs))].title())

    @discord.slash_command()
    async def earth(self, ctx):
        await ctx.respond('Earth: ' + earth_jobs[random.randrange(0, len(earth_jobs))].title())


def setup(bot):
    bot.add_cog(FJF(bot))
