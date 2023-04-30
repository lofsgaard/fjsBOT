from dotenv import load_dotenv
import os
import discord
import logging
from discord.ext import commands
from commands.rekruttering import classes_eq, classes_noggen, classes_savant, classes_of, raid_tider, about

load_dotenv()

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Discord Application secret
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print("Logged in as " + client.user.name)


@client.command(name='clear', help='this command will clear msgs')
@commands.has_role("Vaktmester")
async def clear(ctx):
    await ctx.channel.purge(limit=100)


@client.command()
@commands.has_role("Vaktmester")
async def rekruttering(ctx):
    await clear(ctx)
    await ctx.send(about())
    await ctx.send(raid_tider())
    embed = discord.Embed(title='Hva ser vi etter for øyeblikket', timestamp=ctx.message.created_at)
    embed.set_thumbnail(url='https://raw.githubusercontent.com/Terudo/rabiat-shit/main/Bilder/rabiat_clean.png')
    embed.add_field(name='Team Noggenfoggers', value=classes_noggen(), inline=True)
    embed.add_field(name='Team Exitquit', value=classes_eq(), inline=True)
    embed.add_field(name='\a', value='\a', inline=False)
    embed.add_field(name='Team Oljefondet', value=classes_of(), inline=True)
    embed.add_field(name='Team Savant', value=classes_savant(), inline=True)
    embed.add_field(name='Eksepsjonelle spillere vil alltid vurderes, uavhengig av class', value='', inline=False)
    await ctx.send(embed=embed)


client.run(TOKEN, log_handler=handler)
