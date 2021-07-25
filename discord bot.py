import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import channel
from discord import message
from discord.ext import commands 
import asyncio
import datetime as dt

bot=commands.Bot(command_prefix='[') 

@bot.event
async def on_ready(): 
    print(">> Bot is online <<") 

# Test command
@bot.command(pass_context=True)
async def summer(ctx):
    await ctx.send(file=discord.File(r'/Users/chenguanyu/Desktop/商業デザイン/台藝麥塊/3x/資產 2@3x.png'))
async def on_ready():
    print('目前登入身份：',bot.user)
    game = discord.Game('shiro調教中')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel()
    await channel.send(f'{member}join!')

@bot.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == bot.user:
        return
    #如果以「說」開頭
    if message.content.startswith('說'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦？")
      else:
        await message.channel.send(tmp[1])
    if message.content.startswith('!伺服器維護'):
        tmp = message.content.split(" ",1)
        embed=discord.Embed(title=":zap: 伺服器維護:zap: ", description="", color=0x00ff00)
        embed.add_field(name="作業時間：", value=tmp[1], inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('!公投'):
        tmp = message.content.split(" ",1)
        embed=discord.Embed(title=":ballot_box:公投:ballot_box: ", description="", color=0x00ff00)
        embed.add_field(name="項目：", value=tmp[1], inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('!票'):
        tmp = message.content.split(" ",1)
        embed=discord.Embed(title=" ", description="", color=0x00ff00)
        embed.add_field(name="投票區", value=tmp[1], inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('[summer'):
        tmp = message.content.split(" ",1)
        embed=discord.Embed(title="台藝UHC錦標賽 ", description="台藝麥塊暑期活動", color=0x00ff00)
        embed.add_field(name="活動會有豐厚獎勵，歡迎大家點擊連結報名", value="https://ntuaminecraft.com/index.php/activity/", inline=False)
        await message.channel.send(embed=embed)
    
    await bot.process_commands(message)
        

@commands.command()
async def saxd(self, ctx, massage):
    await ctx.message.delete(self)
    await ctx.sent(massage)


@bot.command()
async def test(ctx):
    await ctx.send('test')


bot.run('ODY4MTg0MDQ0ODI1ODg2NzMw.YPr9Zg.Gw-4VPui8zbJ8dbLMu9haPGm7Tw')

