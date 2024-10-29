import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# トークンを環境変数から取得
import os
bot.run(os.getenv('DISCORD_TOKEN'))
