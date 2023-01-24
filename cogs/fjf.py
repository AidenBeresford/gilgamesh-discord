import random
import discord
from discord.ext import commands

wind_jobs = ('knight', 'monk', 'thief', 'white mage', 'black mage', 'blue mage')
water_jobs = ('red mage', 'time mage', 'summoner', 'berserker', 'mystic knight')
fire_jobs = ('ninja', 'hunter', 'geomancer', 'beastmaster', 'bard')
earth_jobs = ('dragoon', 'samurai', 'dancer', 'chemist')

current_jobs = ['Wind', 'Water', 'Fire', 'Earth']

random.seed()


class FJF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def wind(self, ctx):
        current_jobs[0] = wind_jobs[random.randrange(0, len(wind_jobs)-1)]
        await ctx.respond("Wind: " + current_jobs[0].title())

    @discord.slash_command()
    async def water(self, ctx):
        current_jobs[1] = water_jobs[random.randrange(0, len(water_jobs) - 1)]
        await ctx.respond("Water: " + current_jobs[1].title())

    @discord.slash_command()
    async def fire(self, ctx):
        current_jobs[1] = fire_jobs[random.randrange(0, len(fire_jobs) - 1)]
        await ctx.respond("Fire: " + current_jobs[2].title())

    @discord.slash_command()
    async def earth(self, ctx):
        current_jobs[1] = earth_jobs[random.randrange(0, len(earth_jobs) - 1)]
        await ctx.respond("Earth: " + current_jobs[3].title())


def setup(bot):
    bot.add_cog(FJF(bot))
