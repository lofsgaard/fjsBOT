from dotenv import load_dotenv
import os
import discord

load_dotenv()

# Discord Application secret
TOKEN = os.getenv('TOKEN')


class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = MyBot(intents=intents)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$fireworks'):
        await message.channel.send(':fireworks1337:')


bot.run(TOKEN)
