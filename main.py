from dotenv import load_dotenv
import os
import discord
import logging
from discord import app_commands
from discord.ext import commands
from commands.rekruttering import classes_eq, classes_noggen, classes_savant, classes_of, raid_tider, about

load_dotenv()
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# Discord Application secret
TOKEN = os.getenv('TOKEN')

extensions = ('cogs.flip',)
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name)


@bot.event
async def setup_hook() -> None:
    for extension in extensions:
        await bot.load_extension(extension)


@bot.tree.command(name='clear')
@commands.has_role("Vaktmester")
async def clear(interaction: discord.Interaction):
    await interaction.channel.purge(limit=100)
    await interaction.response.send_message('Channel purged', ephemeral=True)


@bot.tree.command(name='rekruttering')
@commands.has_role("Vaktmester")
async def rekruttering(interaction: discord.Interaction):
    await interaction.channel.purge(limit=100)
    await interaction.response.send_message(about())
    await interaction.followup.send(raid_tider())
    embed = discord.Embed(title='Hva ser vi etter for øyeblikket', timestamp=interaction.created_at)
    embed.set_thumbnail(url='https://raw.githubusercontent.com/Terudo/rabiat-shit/main/Bilder/rabiat_clean.png')
    embed.add_field(name='Team Noggenfoggers', value=classes_noggen(), inline=True)
    embed.add_field(name='Team Exitquit', value=classes_eq(), inline=True)
    embed.add_field(name='\a', value='\a', inline=False)
    embed.add_field(name='Team Oljefondet', value=classes_of(), inline=True)
    embed.add_field(name='Team Savant', value=classes_savant(), inline=True)
    embed.add_field(name='Eksepsjonelle spillere vil alltid vurderes, uavhengig av class', value='', inline=False)
    await interaction.followup.send(embed=embed)


bot.run(TOKEN, log_handler=handler)
