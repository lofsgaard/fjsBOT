import discord
from discord.ext import commands
from discord import app_commands
from commands.rekruttering import classes_eq, classes_noggen, classes_savant, classes_of, raid_tider, about


class Rabiat(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass

    @app_commands.command(name='rekruttering')
    @commands.has_role("Vaktmester")
    async def rekruttering(self, interaction: discord.Interaction):
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


async def setup(bot) -> None:
    await bot.add_cog(Rabiat(bot))
