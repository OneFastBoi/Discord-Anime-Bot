import requests
import discord
from discord.ext import commands,tasks
from discord.utils import get
from bs4 import BeautifulSoup
import time,datetime

class Scrape:
    def __init__(self):
        self.prefix = 'https://www13.9anime.to'
        self.link2match = ''
        self.name = ''
        self.epLinkList = []
    
    def search(self,keyword):
        searchWord,url = '',''
        
        for letter in keyword:
            if letter != ' ':
                searchWord += letter
            else:
                searchWord += '+'

        url = 'https://www12.9anime.to/search?keyword=' + searchWord
        print(url)
        self.page = requests.get(url)
        self.getStatus()
    
    def getStatus(self):
        soup = BeautifulSoup(self.page.content, 'html.parser')
        self.animeList = soup.find_all('ul',{'class':'anime-list'})
        self.epListRaw = self.animeList[0].find_all('div',{'class':'tag ep'})
        self.epLinkRaw = self.animeList[0].find_all('a',{'class':'name'},href = True)
        self.epLinkList.clear()
        for link in self.epLinkRaw: self.epLinkList.append(link['href'])
        self.animeIndex = self.epLinkList.index(self.link2match)
        print(self.animeIndex)

    def getName(self,link):
        nameSplit = link.split('/')
        self.link2match = '/watch/' + nameSplit[nameSplit.index('watch')+1]
        self.name = nameSplit[nameSplit.index('watch')+1].split('.')[0]
        print(self.link2match)

Scrape = Scrape()
client = commands.Bot(command_prefix = '!')
x = True

@client.event
async def on_ready():    
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Kimetsu no Yaiba: Mugen Train"))
    #anime_status.start()
    print('# Core Ready')

@client.command(aliases =['add'])
async def addAnime(ctx,link):
    #https://www13.9anime.to/watch/horimiya.m0o8/ep-1
    Scrape.getName(link)
    Scrape.search(Scrape.name)

@tasks.loop(seconds=60)
async def animeStatus():
    podel = client.get_channel(814250079636553788)
    global x
    try:
        Scrape.search('jujutsu kaisen')
    except:
        print('# exeption')
    if Scrape.epListRaw[2].getText() != 'Ep 19/24' and x:
        x = False
        await podel.send('<@&814246011383054357> Jujutsu kaisen time')
        await podel.send(Scrape.prefix+'/watch/jujutsu-kaisen-tv.32n8')
    else:
        print('# Not released yet')    
    print('# Update time = ' + str(datetime.datetime.now()))

client.run('ODE0MjE2MjUyNTA2NzY3Mzcw.YDan-g.-orrvbKh4J5JvCPOuVoY2BFqmvg')