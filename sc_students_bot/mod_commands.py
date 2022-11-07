import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands

class MemberPurgeWhitelist(commands.Cog):
    """A Cog for purging members based on their roles.

    This Cog allows users to build a whitelist of roles. Then, when the
    :code:`purge` subcommand is run, all users that do not have at least
    one role in the whitelist will be purged (i.e., kicked) from the server.
    """

    # This is the group of Discord slash commands used for purging members based on role
    purge_members_group = SlashCommandGroup("member_purge", "Purge members from server using a role whitelist")

    def __init__(self, bot):
        """Basic constructor for the Cog.

        :param bot: the Bot to which the Cog will be registered
        :type bot: discord.Bot
        """
        self.bot = bot
        self.role_whitelist = []

    @purge_members_group.command(
        description="Adds a role to the purge whitelist. Any user with this role will not be purged"
    )
    async def add_to_whitelist(self, ctx, role: discord.Role):
        """Adds a role to the whitelist.

        :param ctx: the context for the issued command
        :type: ctx: discord.ApplicationContext
        :param role: the role to add to the whitelist
        :type role: discord.Role
        """
        self.role_whitelist.append(role)
        await ctx.respond("Added {} to whitelist".format(role.name))

    @purge_members_group.command(
        description="Removes a role from the purge whitelist"
    )
    async def remove_from_whitelist(self, ctx, role: discord.Role):
        """Remove a role from the whitelist.

        :param ctx: the context for the issued command
        :type: ctx: discord.ApplicationContext
        :param role: the role to remove from the whitelist
        :type role: discord.Role
        """
        response_msg = "Role {} not in whitelist".format(role.name)
        if role in self.role_whitelist:
            self.role_whitelist.remove(role)
            response_msg = "Role {} removed from whitelist".format(role.name)
        await ctx.respond(response_msg)

    @purge_members_group.command(
        description="Clears all roles from the purge whitelist."
    )
    async def clear_whitelist(self, ctx):
        """Clears all roles from the whitelist.

        :param ctx: the context for the issued command
        :type: ctx: discord.ApplicationContext
        """
        self.role_whitelist = []
        await ctx.respond("Whitelist is now empty")

    @purge_members_group.command(
        description="Sends the whitelist to Discord as a message"
    )
    async def view_whitelist(self, ctx):
        """Sends the whitelist to Discord as a message.

        :param ctx: the context for the issued command
        :type: ctx: discord.ApplicationContext
        """
        response_msg = "Roles in whitelist:\n"
        if len(self.role_whitelist) == 0:
            response_msg += "NONE"
        else:
            response_msg += "\n".join(["  * {}".format(r.name) for r in self.role_whitelist])
        await ctx.respond(response_msg)

    @purge_members_group.command(
        description="Purge members that don't have one of the roles in the whitelist"
    )
    async def purge(self, ctx):
        """Purge users that do not have at least one of the roles in the whitelist.

        :param ctx: the context for the issued command
        :type: ctx: discord.ApplicationContext
        """
        if len(self.role_whitelist) == 0:
            await ctx.respond("No roles in whitelist! Aborting purge!")
            return
        server = ctx.guild
        if server is None:
            await ctx.respond("Cannot get guild")
        members_to_purge = []
        for m in server.members:
            if not any([r in self.role_whitelist for r in m.roles]):
                members_to_purge.append(m)
        members_not_purged = [m for m in server.members if m not in members_to_purge]
        with open("to_purge.txt", "w") as f:
            rep = "Would purge:\n"
            rep += "\n".join(["  * {}".format(m.name) for m in members_to_purge])
            f.write(rep)
        with open("no_purge.txt", "w") as f:
            rep = "Would NOT purge:\n"
            rep += "\n".join(["  * {}".format(m.name) for m in members_not_purged])
            f.write(rep)
        await ctx.respond("Test purge successful!")
