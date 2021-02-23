import requests
from bs4 import BeautifulSoup

html = requests.get("https://coinmarketcap.com/")

soup = BeautifulSoup(html.content)

tagBtc = soup.findAll("a",{"href":"/currencies/bitcoin/markets/"})
sayac = 0
for btc in tagBtc:
    yaziBtc = btc.text
    print(yaziBtc)
    sayac +=1
    if sayac == 1:
        break

#eth için
tagEth = soup.findAll("a",{"href":"/currencies/ethereum/markets/"})
sayac1 = 0
for eth in tagEth:
    yaziEth = eth.text
    print(yaziEth)
    sayac1 +=1
    if sayac1 == 1:
        break

#bnb için
tagBnb = soup.findAll("a",{"href":"/currencies/binance-coin/markets/"})
sayac2 = 0
for bnb in tagBnb:
    yaziBnb = bnb.text
    print(yaziBnb)
    sayac2 +=1
    if sayac2 == 1:
        break

#xrp için
tagXrp = soup.findAll("a",{"href":"/currencies/xrp/markets/"})
sayac3 = 0
for xrp in tagXrp:
    yaziXrp = xrp.text
    print(yaziXrp)
    sayac3 += 1
    if sayac3 == 1:
        break

#ltc için
tagLtc = soup.findAll("a",{"href":"/currencies/litecoin/markets/"})
sayac4 = 0
for ltc in tagLtc:
    yaziLtc = ltc.text
    print(yaziLtc)
    sayac4 += 1
    if sayac4 == 1:
        break    
