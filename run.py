import discord

import os

from sc_students_bot import *

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Bot(intents=intents)

define_command(bot, add_role_to_whitelist, pass_context=True)
define_command(bot, remove_role_from_whitelist, pass_context=True)
define_command(bot, view_role_whitelist, pass_context=True)
define_command(bot, purge_role_whitelist, pass_context=True)

if "DISCORD_TOKEN" not in os.environ:
    raise ValueError("DISCORD_TOKEN not set!")

bot.run(os.environ["DISCORD_TOKEN"])
