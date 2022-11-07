from .mod_commands import *

def define_command(bot, command_func, **kwargs):
    """Utility function to add a command to a bot from :code:`run.py`.

    :param bot: the bot to add the command to
    :type bot: discord.Bot
    :param command_func: the function to define as a new command
    :type command_func: Callable[[discord.ApplicationContext, ...], Awaitable[None]]
    :param \**kwargs: keyword arguments to be passed to discord.Bot.command
    :type \**kwargs: Any
    """
    return bot.command(**kwargs)(command_func)
