from discord import message

from i_command import ICommand


class HelpCommand(ICommand):

    def command_name(self):
        return 'help'

    async def execute(self, discord_message: message, parameter):
        command_list_string = [
            '**help** -> lista os comandos disponíveis',
            '**comp _<player#tag>_** -> exibe o status competitivo do player',
            '**comph _<player#tag>_** -> exibe o histórico competitivo do player'
        ]

        await discord_message.channel.send('\n'.join(command_list_string))
