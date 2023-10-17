import os
import random
import asyncio
import typing

import discord
from discord.ext import commands

from datetime import *
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.message_content = True

prefix = '$'
bot = commands.Bot(command_prefix=prefix, intents=intents)

x,y,z = symbols("x y z")

@bot.event
async def on_ready():
    print('以下のユーザーとしてログインしました')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f'Prefix {prefix} | made by Yuki'))

@bot.command()
async def echo(ctx,text:str):
    await ctx.send(text)

@bot.command()
async def math(ctx,mode:str,formula:str,variable:var=None):
    if mode == "calc":
        await ctx.send(str(parse_expr(formula)))
    elif mode == "primef":
        result = factorint(int(formula))
        await ctx.send(result)
        
@bot.command()
async def micalc(ctx,count:int):
    for i in range(count):
        value1 = random.randint(1,10)
        value2 = random.randint(1,10)
        signlist = ["+","-","*","/"]
        value3 = random.choice(signlist)
        calc = str(value1) + value3 + str(value2)
        await ctx.send(calc)

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

bot.run(os.environ.get("BOT_TOKEN"))