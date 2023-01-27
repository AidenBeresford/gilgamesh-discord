import typing

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

    @discord.slash_command(description='Ban a member.')
    async def ban(self, ctx, member: discord.Member,
                  reason: str,
                  deletion_days: typing.Optional[int] = 0):
        await member.ban(delete_message_days=deletion_days, reason=reason)
        await ctx.respond(f'Banned {member.name} for: {reason}')


def setup(bot):
    bot.add_cog(Moderation(bot))
