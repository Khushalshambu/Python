from numpy import product
import requests
from bs4 import BeautifulSoup

baseurl = "https://www.hamleys.in/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

}
r = requests.get("https://www.hamleys.in/toys-by-ages/18-36-months?filter=gender~BOYS")
soup = BeautifulSoup(r.content,'lxml')

productlist = soup.find_all('.trend-price-div')

# productlinks = []
# for item in productlist:
#     for link in item.find_all('a',href=True):
#         productlinks.append(baseurl + link['href'])
for item in productlist:
    print(item)
# print(len(productlinks))