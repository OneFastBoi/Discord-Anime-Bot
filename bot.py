import discord
from discord.ext import commands,tasks
from discord.utils import get
import json,Backend

client = commands.Bot(command_prefix = '!')
x = True

#ping <@id>
@client.event
async def on_ready():
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Kimetsu no Yaiba: Mugen Train"))
    print('# Core Ready')

@client.command(aliases =['add'])
async def addAnime(ctx,link):
    animeName = Backend.getName(link)
    page = Backend.search(animeName)
    data = animeName + ',' + link + ',' + Backend.getStatus(page,link)
    Backend.updateDatabase(data)

@client.command()
async def readList(ctx):
    print(Backend.readFromDatabase())

token = open('token.txt','r+')
client.run(token.read())