from keep_alive import keep_alive
import os
import discord
import requests
import json


client = discord.Client()


def is_message_valid(message):
    
    if message.author == client.user:
        return False
    
    if len(message.content) <= 6:
        return False
   
    if not message.content.startswith('!vava '):
        return False

    return True


async def get_player_data(message, playerNameTag):

    playerInfo = playerNameTag.split('#')
    
    response = requests.get(f'https://api.henrikdev.xyz/valorant/v2/mmr/na/{playerInfo[0]}/{playerInfo[1]}')
    response_json = json.loads(response.text)

    competitive_data = response_json['data']['current_data']
    rank = competitive_data['currenttierpatched']
    tier = competitive_data['currenttier']

    await message.channel.send(f"{playerInfo[0]}#{playerInfo[1]}\nRANK: {rank} ({tier}/100)")
    

@client.event
async def on_ready():
    
    print('Login successful. USER: {0.user}'.format(client))


@client.event
async def on_message(message):
    
    if not (is_message_valid(message)):
        return
    
    args = message.content.split(' ')
    command = args[1]
    parameter = args[2]

    if not (command == 'player-status-comp'):
        await message.channel.send(f"Comando {command} nao cadastrado.")

    await get_player_data(message, parameter)
    


keep_alive()
client.run(os.environ['TOKEN'])