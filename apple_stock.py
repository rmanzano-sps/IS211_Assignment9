# In terminal type python apple_stock.py

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url = urlopen('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')
soup = BeautifulSoup(url, 'html.parser')

tbody_data = soup.find('tbody')

results = []

for td_data in tbody_data:
    try:
        date = td_data.contents[0].contents[0].contents[0]
        close_price = td_data.contents[4].contents[0].contents[0]
    except:
        continue

    results.append([date, close_price])
    # results.append(close_price)

for item in results:
    seperator = ', Close Price: '
    print('Date: ' + seperator.join(item))
