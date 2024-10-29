import discord
from discord.ext import commands
from flask import Flask, request
import os

app = Flask(__name__)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@app.route('/')
def home():
    return "ボットが動作しています！"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

# Discordコグの読み込み
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    
    # jankenコグを読み込む（他のファイルからのインポートは必要）
    if not hasattr(bot, 'janken_loaded'):
        bot.janken_loaded = True
        bot.load_extension('janken')

# トークンを環境変数から取得
bot.run(os.getenv('DISCORD_TOKEN'))

# Flaskをバックグラウンドで起動
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))  # Renderは5000ポートを使用

