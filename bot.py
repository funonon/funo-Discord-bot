import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# janken.pyのコグをセットアップ
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    
    # jankenコグを読み込む
    if not hasattr(bot, 'janken_loaded'):
        bot.janken_loaded = True
        bot.load_extension('janken')

# トークンを環境変数から取得
bot.run(os.getenv('DISCORD_TOKEN'))
