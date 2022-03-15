import os
import re

import discord

from commands import commands
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print('Login successful. USER: {0.user}'.format(client))


@client.event
async def on_message(message):
    message_regex = re.search('(!v)\\s(\\w+)\\s?(.*)', message.content)

    if message.author == client.user:
        return False

    if not message_regex:
        return False

    command = message_regex.group(2)
    parameter = message_regex.group(3)

    executable_command = list(filter(lambda c: c.command_name() == command, commands))

    if not len(executable_command) == 0:
        await executable_command[0].execute(message, parameter)
    else:
        await message.channel.send(f"Comando '{command}' nao cadastrado.\nUtilize o commando '!v help'")


if __name__ == '__main__':
    keep_alive()
    client.run(os.environ['TOKEN'])
