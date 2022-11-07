import discord

import os

# Import cogs, commands, etc. from the sublib
from sc_students_bot import *

# Enable the "members" and "message_content" intents
# Note: requires the Discord Appplication to have the
#       correct permissions
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Create the Bot
bot = discord.Bot(intents=intents)

# Create a MemberPurgeWhitelist to enable the "member_purge" command group
mem_purge_cog = MemberPurgeWhitelist(bot)

# Add commands to Bot
bot.add_cog(mem_purge_cog)

# Make sure a Discord token is provided via environment variable
if "DISCORD_TOKEN" not in os.environ:
    raise ValueError("DISCORD_TOKEN not set!")

# Run the Bot
bot.run(os.environ["DISCORD_TOKEN"])
