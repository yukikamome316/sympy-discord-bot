import discord
from discord.ext import commands
from datetime import datetime

prefix = '_'
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('以下のユーザーとしてログインしました')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f'Prefix {prefix} |This bot is developed'))

bot.run('NTM3ODc4MzAwMDczMjYzMTIy.DyrtQQ.wPe8Go3G9Mnvb5HjQPDfA3Vf0QA')