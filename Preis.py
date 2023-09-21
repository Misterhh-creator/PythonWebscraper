import requests
import datetime
import time
from bs4 import BeautifulSoup
import json
import matplotlib.pyplot as plt
import numpy as np
# 1. Git commit
# 2. Suche aus der Bitcoin Preisliste den max und den min. Wert
# 3. Passe in Zeile 17 die Reichweite des Plots an den min und den max Wert an

def darstellen_als_treppenplot(x: list, y: list):
      plt.style.use('_mpl-gallery') 
      fig, ax = plt.subplots() 
      ax.plot(x, y, linewidth=2.0)
      ax.set(xlim=(0, 220), xticks=np.arange(0, 220), 
             ylim=(27100, 27300), yticks=np.arange(27100, 27300)) #zwischen 0 und 8 in Schritten 1-7
      plt.show()
    

Preisdaten = {}
Anzahl=10
#def scrapebitcoin():
    # def scrapebitcoin(Anzahl: int):

def timesleep():
     time.sleep(10)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/36.0'}

URL = "https://finance.yahoo.com/quote/BTC-USD"

while Anzahl>0:
        Anzahl -= 1

        response = requests.get(URL, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        for x in soup.find_all(name="fin-streamer", attrs={"data-field": "regularMarketPrice", "data-symbol":"BTC-USD"}): #data-field + data-symbol
            #print(time.asctime()+': ' +x.text)
            Preisdaten[int(datetime.datetime.utcnow().timestamp()) % 200] = float(x.text.replace(",",""))
            print(Preisdaten)
        
        timesleep()

x = list(Preisdaten.keys())
y = list(Preisdaten.values())

json = json.dumps(Preisdaten)

f = open("Bitcoin.json","w")
f.write(json)
f.close()

darstellen_als_treppenplot(x, y)






