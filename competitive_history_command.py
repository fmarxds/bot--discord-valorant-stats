import json

import requests
from discord import message

from i_command import ICommand
from valorant_utils import get_player_uuid


class CompetitiveHistoryCommand(ICommand):

    def command_name(self):
        return 'comph'

    async def execute(self, discord_message: message, player_name_tag):
        player_info = player_name_tag.split('#')

        puuid = get_player_uuid(player_info[0], player_info[1])

        response = requests.get(
            f'https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/br/{puuid}?filter=competitive&size=4')
        response_json = json.loads(response.text)

        matches = response_json['data']

        message_output = []

        for match in matches:
            metadata = match['metadata']
            players = match['players']['all_players']
            team_red = match['teams']['red']
            team_blue = match['teams']['blue']

            player = list(filter(lambda player: player['puuid'] == puuid, players))[0]
            player_team = player['team']
            player_stats = player['stats']

            if player_team.lower() == 'red':
                if team_red['has_won']:
                    match_result = f"VITÓRIA ({team_red['rounds_won']}/{team_red['rounds_lost']})"
                else:
                    match_result = f"DERROTA ({team_red['rounds_won']}/{team_red['rounds_lost']})"
            else:
                if team_blue['has_won']:
                    match_result = f"VITÓRIA ({team_blue['rounds_won']}/{team_blue['rounds_lost']})"
                else:
                    match_result = f"DERROTA ({team_blue['rounds_won']}/{team_blue['rounds_lost']})"

            message_output.append(
                f"**# {match_result}**\n"
                f"***MAPA***: `{metadata['map']}`\n"
                f"***AGENTE***: `{player['character']}`\n"
                f"***K/D/A***: `{player_stats['kills']}/{player_stats['deaths']}/{player_stats['assists']}`\n"
                f"***HEADSHOTS***: `{player_stats['headshots']}`\n"
                f"***BODYSHOTS***: `{player_stats['bodyshots']}`\n"
            )

        await discord_message.channel.send("\n".join(message_output))
