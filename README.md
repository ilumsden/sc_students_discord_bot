# Students@SC Discord Bot

This repo contains a bot to provide various services, utilities, capabilities, etc. for the Students@SC Discord.
The sections below explain dependencies, how to run the bot, and available commands.

## Dependencies

This bot has the following dependencies:
* Python 3.8 (or higher)
* [Pycord](https://docs.pycord.dev/en/stable/index.html) v2.0 (or higher)

To install the dependencies (except Python), simply run
```bash
python3 -m pip install -r requirements.txt`
```

## Running the Bot:

Since this bot is not hosted anywhere currently, the first step of running this bot is to create a Bot Account.
To do this, follow the very useful [guide from Pycord](https://docs.pycord.dev/en/stable/discord.html).
Note that this bot requires the `GUILD_MEMBERS` and `MESSAGE_CONTENT` privileged intents.

After creating the bot and adding it to your server, you can launch the bot by running
```bash
DISCORD_TOKEN=<TOKEN GOES HERE> python3 run.py
```
If you save your token into a file, you can replace `<TOKEN GOES HERE>` with `$(cat <PATH TO TOKEN FILE>)`.

Once you launch the bot, you should see it appear in the user list on the right of Discord's window.

## Available Commands

This section list all commands and command groups available at this time.

### Purging Members based on Roles

This command group is used to purge/kick every member in the server that does not have a whitelisted role.

This group consists of 5 subcommands:

```
/member_purge add_to_whitelist <ROLE>
```
Adds the specified role to the whitelist.

```
/member_purge remove_from_whitelist <ROLE>
```
Removes the specified role from the whitelist.

```
/member_purge clear_whitelist
```
Removes all roles from the whitelist.

```
/member_purge view_whitelist
```
Sends a response message containing all whitelisted roles to the channel where this command was issued.

```
/member_purge purge
```
Purges/kicks every member in the server that does not have at least one whitelisted role.
