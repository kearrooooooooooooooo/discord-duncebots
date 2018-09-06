import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from token_key import duncerun

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Hi I'm DunceBot")

@client.event
async def on_message(message):
    if message.content.lower() == "anna":
        await client.send_message(message.channel, ":bear:")
    if message.content.lower() == "kearro":
        await client.send_message(message.channel, ":frog:")
    if message.content.lower() == ".meep":
        await client.send_message(message.channel, "moop")
    if message.content.lower() == ".moop":
        await client.send_message(message.channel, "meep")
    if message.content.lower() == ".meepmoop":
        await client.send_message(message.channel, "meepmoop")

#@client.command()
#async def meep():
    #await client.say('moop')
    
#@client.command()
#async def moop():
    #await client.say('meep')
#play around with client.command() cuz does not work for some reason
client.run(duncerun())
