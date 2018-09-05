import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Hi I'm DunceBot")

@client.event
async def on_message(message):
    if message.content == "anna":
        await client.send_message(message.channel, ":bear:")
    if message.content == "kearro":
        await client.send_message(message.channel, ":frog:")
        
client.run("NDg2ODE4NDE5NDY3ODc4NDAw.DnEqDw.65EWa3bYcbXq2iFJJRAQbn_SAXM")

