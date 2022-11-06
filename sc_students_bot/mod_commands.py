import discord

role_whitelist = []

async def add_role_to_whitelist(ctx, role: discord.Role):
    role_whitelist.append(role)
    await ctx.respond("Added {} to whitelist".format(role.name))

async def remove_role_from_whitelist(ctx, role: discord.Role):
    response_msg = "Role {} not in whitelist".format(role.name)
    if role in role_whitelist:
        role_whitelist.remove(role)
        response_msg = "Role {} removed from whitelist".format(role.name)
    await ctx.respond(response_msg)

async def view_role_whitelist(ctx):
    response_msg = "Roles in whitelist:\n"
    if len(role_whitelist) == 0:
        response_msg += "NONE"
    else:
        response_msg += "\n".join(["  * {}".format(r.name) for r in role_whitelist])
    await ctx.respond(response_msg)

async def purge_role_whitelist(ctx):
    if len(role_whitelist) == 0:
        await ctx.respond("No roles in whitelist! Aborting purge!")
        return
    server = ctx.guild
    if server is None:
        await ctx.respond("Cannot get guild")
    members_to_purge = []
    for m in server.members:
        if not any([r in role_whitelist for r in m.roles]):
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
    await ctx.respond()
