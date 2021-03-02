from bs4 import BeautifulSoup
import requests

def search(keyword):
    searchWord,url = '',''
        
    for letter in keyword:
        if letter != ' ':   searchWord += letter
        else:   searchWord += '+'

    url = 'https://www12.9anime.to/search?keyword=' + searchWord
    page = requests.get(url)
    print(url)
    return page

def getStatus(page,link):
    epLinkList,episodes = [],[]
    soup = BeautifulSoup(page.content, 'html.parser')
    animeList = soup.find_all('ul',{'class':'anime-list'})
    epListRaw = animeList[0].find_all('div',{'class':'tag ep'})
    epLinkRaw = animeList[0].find_all('a',{'class':'name'},href = True)

    for link_ in epLinkRaw: epLinkList.append(link_['href'])
    for ep in epListRaw: episodes.append(ep.getText())

    nameSplit = link.split('/')
    link2match = '/watch/' + nameSplit[nameSplit.index('watch')+1]
    index = epLinkList.index(link2match)

    return episodes[index]

def getIndex(page):
    pass

def getName(link):
    nameSplit = link.split('/')
    link2match = '/watch/' + nameSplit[nameSplit.index('watch')+1]
    name = nameSplit[nameSplit.index('watch')+1].split('.')[0]
    return name

def updateDatabase(data):
    anim = open('animeList.anim','r')
    with open('animeList.anim','a') as fl:
        if data in anim.read():
            print('already in list')                
        else:
            fl.write(str(data))
    fl.close()
    anim.close()                

def readFromDatabase():
    with open('animeList.anim','r+') as fl:
        return fl.read()

