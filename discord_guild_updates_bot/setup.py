from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='discord-guild-updates-bot',
    version='1.0',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'discord-guild-updates = discord_guild_updates_bot.main:main',
        ],
    },
)
