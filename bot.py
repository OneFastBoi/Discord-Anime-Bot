import requests
import discord
from discord.ext import commands,tasks
from discord.utils import get
from bs4 import BeautifulSoup
import time,datetime

class Scrape:
    def __init__(self):
        self.prefix = 'https://www13.9anime.to'
    
    def search(self,keyword):
        searchWord,url = '',''
        
        for letter in keyword:
            if letter != ' ':
                searchWord += letter
            else:
                searchWord += '+'

        url = 'https://www12.9anime.to/search?keyword=' + searchWord
        self.page = requests.get(url)
        self.getStatus()
    
    def getStatus(self):
        soup = BeautifulSoup(self.page.content, 'html.parser')
        self.animeList = soup.find_all('ul',{'class':'anime-list'})
        self.epListRaw = self.animeList[0].find_all('div',{'class':'tag ep'})  
        print('# Update complete')  

Scrape = Scrape()
client = commands.Bot(command_prefix = '!')
x = True


@client.event
async def on_ready():    
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Kimetsu no Yaiba: Mugen Train"))
    anime_status.start()
    print('# Core Ready')    

@tasks.loop(seconds=60)
async def anime_status():
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

client.run('ODE0MjE2MjUyNTA2NzY3Mzcw.YDan-g.FXQ9avmXJu9ivR4eBNg6vH-NBXk')