# Discord_guild_updates_bot

I got tired of slow RSS feeds or 3rd party guild monitoring sites not showing me the most up to date or accurate version of my guilds roster, so I decided to build my own guild notification bot. This bot is designed to fetch any changes to your World of Warcraft guild roster. The bot is running in the cloud and checks for an update once every 6 hours. It could be configued to run on a more frequent schedule, but money :^)

# Prerequisites

1) You will need to have a Discord bot added to your server
2) You will need to replace in the code your bot token and channel ID (where the bot will post)
3) This bot makes use of the Blizzard API
4) You will need to add your own API oAuth credentials
5) Make note of the baseUrl. If you are in the US, you need to update the URL to use us.api.blizzard.com instead
6) You will need to edit the guild URI to include your guild. You can use this format
   ```
   'data/wow/guild/REALM/GUILD-NAME/roster?namespace=profile-eu&locale=en_EU'
   ```

7) You will need some emojis to represent the classes in wow. What I did was add each class as an emoji to my server and save their id's in a list.

This project will create a text file called members.txt. This text file will be used as a baseline comparison for when the Blizzard API is called. When we call the API, we take the results from the API and compare them with the local file to look for changes. If there is a new entry in the API that is not in our local file, it means that someone has joined the guild. If we see the opposite, it means someone has left. Once we finish our comparison then the API response is written to members.txt and it becomes our new baseline for when this is next run. Example below of what members.txt looks like.
```
[[{"name": "test1", "class": 5}], [{"name": "test2", "class": 9}], [{"name": "test3", "class": 8}], [{"name": "test4", "class": 2}], [{"name": "test5", "class": 8}]]
```

# Using the Bot

If you want, you can simply just run the bot whenever you please by triggering main.py, but the deployment I originally decided to go for was to create a simple **.bat** script to trigger the code when Discord is opened. Now I have the bot running in the cloud and this is not necessary with nohup, but you can copy the below and edit where your main.py is running from and where Discord.exe is opened from.

```
@echo off
start "" "C:\Users\user\path\to\discord.exe"
python "C:\Users\user\path\to\main.py"
```

# Improvements

~~You'll notice that currently the class id's are not being used by the bot. My goal for this is to deploy a solution that when a joiner / leaver message is posted the class id will be used to alter the colour of the message so that we can tell the class of the person who joined / left~~ COMPLETE ! Now when someone joins or leaves their class emoji is included in the message.

~~Another goal is to make it so that after the initial execution on startup, the bot will periodically check against the Blizzard API to see if there were any updates throughout the day. This should really only have to be done once or twice during the day as updates can be slow to reach the API~~ COMPLETE ! Now the bot will run every six hours and is now hosted in the cloud so it is not relient on my local machine to run.

Further improvements will be looking deeper into the Blizzard API to see what extra functionality is available. I would like to be able to automatically set notes on new members or alter their in-game rank, but we will have to see what limits are available.

Currently working on getting the bot to be automatically deployed to Hetzner cloud upon a push to the repo being made. Currently configuring a .deb package to be created and will then be focusing on server deployment with Terraform.


# Other Notes

This bot was just a bit of fun and something to kill some time. It is by no means optimized and there are many improvements I want to make to the structure of the code, but for now it works and it will help keep myself and my guild officers informed on any new joiners / leavers in the guild
