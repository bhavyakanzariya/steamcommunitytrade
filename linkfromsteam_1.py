# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:40:05 2019

@author: Bhavya
"""

import requests
import bs4
#import re
import codecs
#import webbrowser


#myfile = open ("htmltext.txt","w",errors='ignore')
f = codecs.open("1.html",'r',encoding='utf-8', errors='ignore')
#print (f.read())


url  = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Spray&appid=730#p1_price_asc'
response = requests.get(url)
soup  = bs4.BeautifulSoup(f.read(),"html.parser")
x = soup.find_all('a')
a = []
b = []
for bracket in x:
    a.append(bracket.get('href'))
    

for link in a:
    if "https://steamcommunity.com/market/listings/730/Sealed%20Graffiti" in link:
        b.append(link)
        
print (b, len(b))
        

#myfile.write(response.text)
#myfile.close
#for link in a:
    #webbrowser.open_new_tab(link)
    