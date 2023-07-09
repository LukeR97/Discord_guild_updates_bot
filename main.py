import requests
from urllib.parse import urljoin
import json
import discord
from discord.ext import commands
import vars

#==========================================================
# CONFIG
baseUrl = 'https://eu.api.blizzard.com/'
guildURI = vars.guildURI
CLIENT_ID = vars.CLIENT_ID
CLIENT_SECRET = vars.CLIENT_SECRET
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
#==========================================================

# Our only bot event on startup
@bot.event
async def on_ready():
    channel = bot.get_channel(1120406484015124560)

    data = {'grant_type': 'client_credentials',}

    response = requests.post('https://oauth.battle.net/token', data=data, auth=(f'{CLIENT_ID}', f'{CLIENT_SECRET}'))
    auth = response.json()
    access_token = auth['access_token']

    headers = {'Authorization': f'Bearer {access_token}',}

    params = {'namespace': 'dynamic-eu',}

    # Blizzard API to pull the most up to date version of guild members
    guildResp = requests.get(urljoin(baseUrl, guildURI), params=params, headers=headers)
    members = guildResp.json()
    guildies = list()

    # filter out the member names and their class id's from the list
    for member in members['members']:
        name = member['character']['name']
        playerClass = member['character']['playable_class']['id']
        guildies.append([{'name': name, 'class':playerClass}])


    json_data = json.dumps(guildies, ensure_ascii=False)

    # Get the local version of the guild member list
    # If members.txt does not exist. Create a master file to use at the base
    try:
        with open("members.txt", "r", encoding="utf-8") as tfile:
            file_content = tfile.read()
            tfile.close()
    except FileNotFoundError:
        print("No base found. Creating base.")
        with open('members.txt', 'w', encoding='utf-8') as tfile:
            tfile.write(json_data + '\n')
            tfile.close()
    finally:
        with open("members.txt", "r", encoding="utf-8") as tfile:
            file_content = tfile.read()
            tfile.close()


    file_content_json = json.loads(file_content)

    new_additions = []
    leavers = []

    # Here we find any differences between our local list and the API list
    # If there are any new additions in the API, it means that someone has joined the guild
    # If there is an entry in the local version that is not in the API, it means someone has left
    # the guild
    for item in guildies:
        if item not in file_content_json:
            new_additions.append(item)

    for item in file_content_json:
        if item not in guildies:
            leavers.append(item)

    # This code is for filtering out only the names from the JSON list.
    # I have plans to incorporate the class ID's to send a coloured message based
    # on the class ID, but for now we only use the names
    new_additions_json = json.dumps(new_additions)
    new_additions_json = json.loads(new_additions_json)
    new_name_values = [item[0]['name'] for item in new_additions_json]

    leavers_json = json.dumps(leavers)
    leavers_json = json.loads(leavers_json)
    leaver_name_values = [item[0]['name'] for item in leavers_json]


    # VERY IMPORTANT - We now need to save the API list to our local list as this will now
    # become the new local version and the next time we run this code, it will be compared with
    # the most up to date API version
    if new_additions != [] or leavers != []:
        with open('members.txt', 'w', encoding='utf-8') as tfile:
            tfile.write(json_data + '\n')
            tfile.close()

    # Here we post our output to the discord channel. Simply if there has been someone who joined
    # we send the list of joiners in green and any leavers in red
    if channel:
        if new_additions != []:
            color = discord.Color.from_rgb(0, 255, 0)
            for n in new_name_values:
                embed = discord.Embed(description=str(n) + " Joined the guild!", color=color)
                await channel.send(embed=embed)
        if leavers != []:
            color = discord.Color.from_rgb(255, 0, 0)
            for n in leaver_name_values:
                embed = discord.Embed(description=str(n) + " Left the guild!", color=color)
                await channel.send(embed=embed)
        await bot.close()
    else:
        print("channel not found")

bot.run(vars.TOKEN)