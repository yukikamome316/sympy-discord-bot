import discord
from discord.ext import commands
from datetime import *
import numpy
from sympy import *
import random
import asyncio
import typing

prefix = '$'
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('以下のユーザーとしてログインしました')
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
        try:
            msg = await ctx.wait_for('message',timeout=10.0,check=check)
        except TimeoutError:
            await ctx.send('けいさんおそーいw')
        else:
            pass

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx,members: commands.Greedy[discord.Member], *,reason:typing.Optional[str] = 0):
    for member in members:
        await ctx.send(f'{member.mention}さんをKickしたよ！ 理由:{reason}')
        await member.kick(reason=reason)

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, members: commands.Greedy[discord.Member],delete_days: typing.Optional[int] = 0, *,reason: str):
    for member in members:
        await ctx.send(f'{member.mention}さんをBanしたよ！')
        await member.ban(delete_message_days=delete_days, reason=reason)

bot.run('NTM3ODc4MzAwMDczMjYzMTIy.DyrtQQ.wPe8Go3G9Mnvb5HjQPDfA3Vf0QA')