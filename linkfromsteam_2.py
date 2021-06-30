# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:25:29 2019

@author: Bhavya
"""
"""
@author notes:
    feel free to use this program whenever you like.
    "steamcopies.txt" contains all the link I could get.
    run the program first and then use linkremover funtion with the filename
   of files containing current buy orders record to remove current buy orders link
    
    after that you have Executer function at your disposal to make the buy orders.


"""


"""
current status : I have done buy orders till executer(11), continue from (12)

commands:: linkremover("currentbuyorders.txt")
           check if len(c) is approximately correct
           Executer from 0 to proper number will jump start the process

"""
#import requests
import bs4
import codecs
import webbrowser

f = codecs.open("steamcopies.txt",'r',encoding='utf-8', errors='ignore')

soup  = bs4.BeautifulSoup(f.read(),"html.parser")
x = soup.find_all('a')
a = []
b = []
c = []
for bracket in x:
    a.append(bracket.get('href'))
    

for link in a:
    if "https://steamcommunity.com/market/listings/730/Sealed%20Graffiti" in link:
        b.append(link)
        
print (len(b))

for link in b:
    if link not in c:
        c.append(link)
        

print (len(c))

def linkremover(filename):
    funf = codecs.open(filename,'r',encoding='utf-8', errors='ignore')

    funsoup  = bs4.BeautifulSoup(funf.read(),"html.parser")
    funx = funsoup.find_all('a')
    funa = []
    for bracket in funx:
        funa.append(bracket.get('href'))
    

    for link in funa:
        if "https://steamcommunity.com/market/listings/730/Sealed%20Graffiti" in link:
            if link in c:
                c.remove(link)
                
    print(len(c))

        
def Executer(number):   #add the not enough links clause to use it till the very end
    n = 50*number       #dynamic number to adujust to the requirements
    for i in range(n,n+50):
        webbrowser.open_new_tab(c[i])