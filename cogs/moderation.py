import typing

import discord
from discord.ext import commands
from discord.ext.commands import errors


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description='Kicks a user.')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member,
                   reason: str):
        try:
            await member.kick(reason=reason)
        except errors.MissingPermissions:
            await ctx.respond("You don't have permission to do that.")
        else:
            await ctx.respond(f'Kicked {member.name} for: {reason}')

    @discord.slash_command(description='Bans a member.')
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

    @discord.slash_command(description='Gives a member a role.')
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member,
                   role: discord.Role):
        try:
            await member.add_roles(role)
        except errors.MissingPermissions:
            await ctx.respond("You don't have permission to do that.")
        else:
            await ctx.respond(f'{member} given the {role} role.')

    @discord.slash_command(description='Removes a member a role.')
    @commands.has_permissions(manage_roles=True)
    async def unrole(self, ctx, member: discord.Member,
                     role: discord.Role,
                     reason: typing.Optional[str] = "None provided."):
        try:
            await member.remove_roles(role, reason=reason)
        except errors.MissingPermissions:
            await ctx.respond("You don't have permission to do that.")
        else:
            await ctx.respond(f'Removed {role} role from user {member} for reason: {reason}')


def setup(bot):
    bot.add_cog(Moderation(bot))
