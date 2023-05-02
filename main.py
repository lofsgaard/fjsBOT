from dotenv import load_dotenv
import os
import discord
import logging
from discord.ext import commands

load_dotenv()
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# Discord Application secret
TOKEN = os.getenv('TOKEN')

extensions = ('cogs.flip', 'cogs.tools', 'cogs.rabiat')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name)


@bot.event
async def setup_hook() -> None:
    for extension in extensions:
        await bot.load_extension(extension)


bot.run(TOKEN, log_handler=handler)
