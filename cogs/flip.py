from discord.ext import commands
import random


class Flip(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass

    @commands.command()
    async def flip(self, ctx: commands.Context) -> None:
        await ctx.send(tossCoin())


async def setup(bot) -> None:
    await bot.add_cog(Flip(bot))


def tossCoin():
    return random.choice(["Heads", "Tails"])
