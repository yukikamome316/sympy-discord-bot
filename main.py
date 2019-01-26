import discord
from discord.ext import commands
from datetime import *
import numpy
from sympy import *
import asyncio
import random

prefix = '$'
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('以下のユーザーとしてログインしまqした')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f'Prefix {prefix} |This bot is developed'))

@bot.command()
async def echo(ctx,text:str):
    await ctx.send(text)

@bot.command()
async def calc(ctx,formula:str):
    try:
        await ctx.send(eval(str(formula)))
    except Exception as e:
        await ctx.send("(!)なにこれ\n" + e.args)

@bot.command()
async def micalc(ctx,count:int):
    for i in range(count):
        value1 = random.randint(1,10)
        value2 = random.randint(1,10)
        signlist = ["+","-","*","/"]
        value3 = random.choice(signlist)
        calc = str(value1) + value3 + str(value2)
        result = eval(calc)
        await ctx.send(calc)
        
        def check(m):
            return m.content == result

        msg = await ctx.wait_for('message', check=check,)
        await ctx.send()
        


@bot.command()
async def kick(ctx,user:discord.user,text:str):
    await ctx.guild.kick(user,reason=text)
    await ctx.send(f'{user}をKickしました。理由:{reason}')

@bot.command()
async def ban(ctx,user:discord.user,text:str):
    await ctx.guild.ban(user,reason=text)
    await ctx.send(f'{user}をKickしました。理由:{reason}')



bot.run('NTM3ODc4MzAwMDczMjYzMTIy.DyrtQQ.wPe8Go3G9Mnvb5HjQPDfA3Vf0QA')