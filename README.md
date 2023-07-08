# Discord_guild_updates_bot

I got tired of slow RSS feeds or 3rd party guild monitoring sites not showing me the most up to date or accurate version of my guilds roster, so I decided to build my own guild notification bot. This bot is designed to fetch any changes to your World of Warcraft guild roster. The bot is currently run locally from my machine and with the use of a simple batch script will execute upon launching Discord.

# Prerequisites

1) You will need to have a Discord bot added to your server
2) You will need to replace in the code your bot token and channel ID (where the bot will post)
3) This bot makes use of the Blizzard API
4) You will need to add your own API oAuth credentials
5) Make note of the baseUrl. If you are in the US, you need to update the URL to use us.api.blizzard.com instead
6) You will need a base reference member list. See below for the format

The reason for this formatting is that when we pull the list of members in the guild from the Blizzard API, we filter out the data we don't care about and just capture the player names and class id's.
This is then stored locally so that the next time we run the code, we have a baseline to compare to and check for any changes (leavers / joiners). This template should be saved as a members.txt file
```
[[{"name": "test1", "class": 5}], [{"name": "test2", "class": 9}], [{"name": "test3", "class": 8}], [{"name": "test4", "class": 2}], [{"name": "test5", "class": 8}]]
```

# Using the Bot

If you want, you can simply just run the bot whenever you please by triggering main.py, but the deployment I decided to go for was to create a simple **.bat** script to trigger the code when Discord is opened. You can copy the below and edit where your main.py is running from and where Discord.exe is opened from

```
@echo off
start "" "C:\Users\user\path\to\discord.exe"
python "C:\Users\user\path\to\main.py"
```

# Improvements

You'll notice that currently the class id's are not being used by the bot. My goal for this is to deploy a solution that when a joiner / leaver message is posted the class id will be used to alter the colour of the message so that we can tell the class of the person who joined / left

Another goal is to make it so that after the initial execution on startup, the bot will periodically check against the Blizzard API to see if there were any updates throughout the day. This should really only have to be done once or twice during the day as updates can be slow to reach the API


# Other Notes

This bot was just a bit of fun and something to kill some time. It is by no means optimized and there are many improvements I want to make to the structure of the code, but for now it works and it will help keep myself and my guild officers informed on any new joiners / leavers in the guild
