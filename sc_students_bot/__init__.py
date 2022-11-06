from .mod_commands import *

def define_command(bot, command_func, **kwargs):
    return bot.command(**kwargs)(command_func)
