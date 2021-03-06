import json

import requests
from discord import message

from i_command import ICommand


class CompetitiveStatusCommand(ICommand):

    def command_name(self):
        return 'comp'

    async def execute(self, discord_message: message, player_name_tag):
        player_info = player_name_tag.split('#')

        response = requests.get(f'https://api.henrikdev.xyz/valorant/v1/mmr/br/{player_info[0]}/{player_info[1]}')
        response_json = json.loads(response.text)

        competitive_data = response_json['data']
        rank = competitive_data['currenttierpatched']
        level = competitive_data['ranking_in_tier']
        last_game = competitive_data['mmr_change_to_last_game']

        output = \
            f"***PLAYER***: `{player_name_tag}`\n" \
            f"***RANK***: `{rank}`\n" \
            f"***PONTOS***: `{level}`\n" \
            f"***ULTIMO JOGO***: `{last_game}`\n"

        await discord_message.channel.send(output)
