import discord
from discord.ext import commands
from datetime import datetime

prefix = '$'
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('以下のユーザーとしてログインしました')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f'Prefix {prefix} |This bot is developed'))

@bot.commands
async def echo(ctx,text:str):
    await ctx.send(text)

@bot.commands
async def calc(ctx,formula:str):
    await ctx.send(eval(formula))

@bot.commands
async def kick(ctx,user:discord.user,text:str):
    await ctx.guild.kick(user,reason=text)
    await ctx.send(f'{user}をKickしました。理由:{reason}')

@bot.commands
async def ban(ctx,user:discord.user,text:str):
    await ctx.guild.ban(user,reason=text)
    await ctx.send(f'{user}をKickしました。理由:{reason}')



bot.run('NTM3ODc4MzAwMDczMjYzMTIy.DyrtQQ.wPe8Go3G9Mnvb5HjQPDfA3Vf0QA')