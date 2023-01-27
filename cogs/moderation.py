import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description='Kick a user.')
    async def kick(self, ctx, member: discord.Member,
                   reason: str):
        await member.kick(reason=reason)
        await ctx.respond(f'Kicked {member.name} for: {reason}')


def setup(bot):
    bot.add_cog(Moderation(bot))
