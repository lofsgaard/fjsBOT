import discord
from discord.ext import commands
from discord import app_commands
from commands.rekruttering import classes_eq, classes_noggen, classes_of, raid_tider, about


class Rabiat(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass

    @app_commands.command(name='rekruttering')
    @commands.has_role("Vaktmester")
    async def rekruttering(self, interaction: discord.Interaction):
        informasjon = self.bot.get_channel(1103279948254416956)
        await informasjon.purge()
        rekrutteringc = self.bot.get_channel(1103280124847214592)
        await rekrutteringc.purge()
        await informasjon.send(about())
        await rekrutteringc.send(raid_tider())
        embed = discord.Embed(title='Hva ser vi etter for øyeblikket', timestamp=interaction.created_at)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/Terudo/rabiat-shit/main/Bilder/rabiat_clean.png')
        embed.add_field(name='Team Noggenfoggers', value=classes_noggen(), inline=True)
        embed.add_field(name='Team Exitquit', value=classes_eq(), inline=True)
        embed.add_field(name='Team Oljefondet', value=classes_of(), inline=True)
        embed.add_field(name='Eksepsjonelle spillere vil alltid vurderes, uavhengig av class', value='', inline=False)
        await rekrutteringc.send(embed=embed)
        await interaction.response.send_message('Channels updated', ephemeral=True)


async def setup(bot) -> None:
    await bot.add_cog(Rabiat(bot))
