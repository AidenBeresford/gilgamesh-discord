import typing

import discord
from discord.ext import commands
from discord.ext.commands import errors


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description='Kick a user.')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member,
                   reason: str):
        try:
            await member.kick(reason=reason)
        except errors.MissingPermissions:
            await ctx.respond("You don't have permission to do that.")
        else:
            await ctx.respond(f'Kicked {member.name} for: {reason}')

    @discord.slash_command(description='Ban a member.')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member,
                  reason: str,
                  deletion_days: typing.Optional[int] = 0):
        try:
            await member.ban(delete_message_days=deletion_days, reason=reason)
        except errors.MissingPermissions:
            await ctx.respond("You don't have permission to do that.")
        else:
            await ctx.respond(f'Banned {member.name} for: {reason}')


def setup(bot):
    bot.add_cog(Moderation(bot))
