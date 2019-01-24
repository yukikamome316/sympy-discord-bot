import discord
from discord.ext import commands
from datetime import datetime

prefix = '_'
default = f'Prefix:{prefix} | by NaGisA & Moriumi'
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('起動しました')
    channel = bot.get_channel(536438078907351041)
    await channel.send('起動しました')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=default))

@bot.event
async def on_member_join(member):
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    channel = bot.get_channel(536438078907351041)
    join = discord.Embed(description=f"{member}", color=0xff69b4)
    join.set_author(name='ユーザーが参加しました！', icon_url=member.avatar_url)
    join.add_field(name="日時", value=f"{date}")
    await channel.send(embed=join)

@bot.event
async def on_member_remove(member):
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    channel = bot.get_channel(536438078907351041)
    leave = discord.Embed(description=f"{member}", color=0xff69b4)
    leave.set_author(name='ユーザーが退室しました！', icon_url=member.avatar_url)
    leave.add_field(name="日時", value=f"{date}")
    await channel.send(embed=leave)

@bot.event
async def on_message(message):
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    file = open('log.txt', 'a')
    string_list = [f'\n{date}'' ''{0.guild}.{0.channel}.{0.author}.{0.content}']
    file.writelines(string_list)

    yuca = bot.get_user(536438078907351041)

    moriumi = 'https://cdn.discordapp.com/attachments/518582047661490192/518582132432437273/moriumi2.png'
    emori = discord.Embed(title='！！！もりうみタイム！！！', description='！！！もりうみタイム！！！')
    emori.set_author(name='！！！もりうみタイム！！！', icon_url=f'{moriumi}')
    emori.set_thumbnail(url=f'{moriumi}')
    emori.set_image(url=f'{moriumi}')
    emori.set_footer(text='！！！もりうみタイム！！！', icon_url=f'{moriumi}')

    if message.author == bot.user and message.content == "リアクションを追加してください":
        await message.add_reaction('🇦')
        await message.add_reaction('🇧')

    if message.author == bot.user or message.author == yuca:
        return

    if message.content.endswith('そうだよ') or message.content.endswith('そうだね') or message.content.endswith('そうだな'):
        await message.channel.send('そうだよ(便乗)')
    elif 'ワイナイナ' in message.content:
        await message.channel.send('コーヒー豆ブライアン')
    elif '小峠' in message.content:
        await message.channel.send('イニエスタ')
    elif message.content.startswith('<@518308798922752011>'):
        await message.channel.send('Hi! :slight_smile: ')
    elif 'もりうみタイム' in message.content:
        await message.channel.send(embed=emori)

    #log = discord.Embed(title="Server", description="{0.guild}".format(message))

    #log.add_field(name="Channel", value="{0.channel}".format(message))
    #log.add_field(name="User", value="{0.author}".format(message))
    #log.add_field(name="Message", value="{0.content}".format(message))

    #channel = discord.utils.get(bot.get_all_channels(), name='yuca-log')
    #await channel.send(embed=log)

    await bot.process_commands(message)

@bot.command()
async def embed(ctx, etitle: str, edesc: str):
    e = discord.Embed(title=f'{etitle}', description=f'{edesc}')
    e.set_author(name=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=e)

@bot.command()
async def poll(ctx, ptitle: str, choice1: str, choice2: str):
    p = discord.Embed(title=f'{ptitle}')
    #p.set_author(name=f'{ptitle} - {ctx.author}', icon_url=f'{ctx.author.avatar_url}')
    p.add_field(name=f'{choice1}', value=':regional_indicator_a:')
    p.add_field(name=f'{choice2}', value=':regional_indicator_b:')
    p.set_footer(text=f'Written by {ctx.author}', icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=p)
    await ctx.send("リアクションを追加してください")

@bot.command()
async def replay(ctx, text: str):
    await ctx.send(f'{text}')

@bot.command()
async def kick(ctx, userName: discord.User):
    await ctx.guild.kick(userName)
    await ctx.send(f'{userName}をKickしました。')

@bot.command()
async def ban(ctx, userName: discord.User):
    await ctx.guild.ban(userName)
    await ctx.send(f'{userName}をBanしました。')

@bot.command()
async def calc(ctx,text:str):
    await ctx.send(eval(text))

@bot.command()
async def game(ctx, playgame: str):
    await ctx.send(f'プレイ中のゲームを``{playgame}``に変更しました。')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f'{playgame}'))

@bot.command()
async def gamereset(ctx):
    await ctx.send(f'プレイ中のゲームを``{default}``に戻しました。')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f'{default}'))

@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！ :smiley: ")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Yuca", description="Pythonで作られたBotです！", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="NaGisA & Moriumi")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Yucaのサーバー参加数", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="招待", value="https://discordapp.com/api/oauth2/authorize?client_id=516910434939306044&permissions=8&scope=bot")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Yuca:Pythonで作られたBotです！", description="", color=0xbb00ee)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/518582047661490192/518650251293229056/yuca500x500alpha.png")
    embed.add_field(name="Prefix", value=f"コマンドの最初に置く文字は``{prefix}``です。", inline=False)
    embed.add_field(name="hello", value=f"挨拶をしてくれます。", inline=False)
    embed.add_field(name="calc", value=f"数式の演算をしてくれます。", inine=False)
    embed.add_field(name="poll", value=f"投票機能です。手軽に投票ができます。使用例：``{prefix}poll タイトル 選択肢１ 選択肢２``")
    embed.add_field(name="embed", value=f"埋め込みメッセージ機能です。使用例：``{prefix}embed タイトル 説明``")
    embed.add_field(name="game", value=f"プレイ中のゲームの表示を変更します。使用例：``{prefix}game 文字列``", inline=False)
    embed.add_field(name="embed", value=f"Embedを表示します。使用例：``{prefix}embed タイトル 説明``", inline=False)
    embed.add_field(name="info", value="Yucaについて表示します。", inline=False)
    embed.add_field(name="help", value="各コマンドのヘルプを表示します。", inline=False)

    await ctx.send(embed=embed)

bot.run('NTM3ODc4MzAwMDczMjYzMTIy.DyrtQQ.wPe8Go3G9Mnvb5HjQPDfA3Vf0QA')