import discord
from discord.ext import commands
import os

# 環境変数からボットのトークンを取得
TOKEN = os.getenv("DISCORD_TOKEN")

# Botの接頭辞とインテントを設定
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ボット起動時のイベント
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Pingコマンドの例
@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")

# メッセージ受信時の処理
@bot.event
async def on_message(message):
    # ボット自身のメッセージには反応しない
    if message.author == bot.user:
        return
    # 他のコマンドを処理
    await bot.process_commands(message)

# Botを実行
bot.run(TOKEN)
