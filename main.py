import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'機器人已上線：{bot.user}')

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"已加入 {channel.name} 開始掛機！")
    else:
        await ctx.send("你需要先加入一個語音頻道，我才能進去陪你喔！")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("已離開語音頻道。")
    else:
        await ctx.send("我不在任何語音頻道中！")

# 啟動防休眠網頁伺服器
keep_alive()
# 啟動機器人
bot.run(os.environ.get('TOKEN'))
