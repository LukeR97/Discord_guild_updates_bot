from setuptools import setup, find_packages

setup(
    name='discord-guild-updates-bot',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'discord-guild-updates = Discord_guild_updates_bot.main:main',
        ],
    },
)
