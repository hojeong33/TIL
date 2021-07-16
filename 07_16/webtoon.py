import requests
from bs4 import BeautifulSoup

url='https://comic.naver.com/index'

response=requests.get(url).text

data=BeautifulSoup(response,'html.parser')

ranking=data.select('#realTimeRankFavorite > li > a')

for rank,name in enumerate(ranking):
    print(rank+1,name.text)
