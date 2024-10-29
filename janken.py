import discord
from discord.ext import commands
import random

class Janken(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="じゃんけん", description="じゃんけんをします！")
    async def janken(self, ctx, choice: str):
        choices = ["グー", "チョキ", "パー"]
        bot_choice = random.choice(choices)
        
        if choice not in choices:
            await ctx.respond("選択肢は「グー」、「チョキ」、または「パー」のいずれかです。")
            return
        
        result = self.determine_winner(choice, bot_choice)

        await ctx.respond(f"あなたの選択: {choice}\nボットの選択: {bot_choice}\n結果: {result}")

    def determine_winner(self, player, bot):
        if player == bot:
            return "引き分け！"
        elif (player == "グー" and bot == "チョキ") or (player == "チョキ" and bot == "パー") or (player == "パー" and bot == "グー"):
            return "あなたの勝ち！"
        else:
            return "あなたの負け！"

def setup(bot):
    bot.add_cog(Janken(bot))
