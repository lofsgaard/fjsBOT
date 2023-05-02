import discord
from discord.ext import commands
from discord import app_commands


class Tools(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass

    @app_commands.command(name='clear')
    @commands.has_role("Vaktmester")
    async def clear(self, interaction: discord.Interaction):
        await interaction.channel.purge(limit=100)
        await interaction.response.send_message('Channel purged', ephemeral=True)


async def setup(bot) -> None:
    await bot.add_cog(Tools(bot))
