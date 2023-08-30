import requests
import time
from bs4 import BeautifulSoup
import json


Anzahl = 10 
Preisdaten={}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/36.0'}

URL = "https://finance.yahoo.com/quote/BTC-USD"

while Anzahl>0:
    Anzahl -= 1

    response = requests.get(URL, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    for x in soup.find_all(name="fin-streamer", attrs={"data-field": "regularMarketPrice", "data-symbol":"BTC-USD"}): #data-field + data-symbol
        #print(time.asctime()+': ' +x.text)
        Preisdaten[time.asctime()] = x.text
        print(Preisdaten)
    
    time.sleep(5)

json = json.dumps(Preisdaten)

f = open("Bitcoin.json","w")
f.write(json)
f.close()


