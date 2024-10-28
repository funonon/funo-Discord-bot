import os
import discord
from discord.ext import commands

# Botのプレフィックス（コマンドの前に付ける文字）を指定
bot = commands.Bot(command_prefix="!")

# Botが起動したときに表示されるメッセージ
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# 簡単なコマンド "!hello" を定義
@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！私はDiscordボットです！")

# メッセージを自動で反応させる
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "こんにちは" in message.content:
        await message.channel.send("こんにちは！元気ですか？")

    # 他のコマンドが動作するための処理
    await bot.process_commands(message)

# Botを実行（トークンを環境変数から取得）
bot.run(os.getenv("DISCORD_TOKEN"))
