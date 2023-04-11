from requests_html import HTMLSession
from bs4 import BeautifulSoup


s = HTMLSession()

url = 'https://www.amazon.in/s?k=kids+toys&crid=2OGG7AGYF9RCI&sprefix=kids+toy%2Caps%2C184&ref=nb_sb_noss_1'

def getdata(url):
    r = s.get(url)
    # r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getnextpage(soup):
    # this will return the next page URL
    pages = soup.find('ul', {'class': 's-pagination-strip'})
    if not pages.find('li', {'class': 's-pagination-item s-pagination-next s-pagination-disabled'}):
        url = 'https://www.amazon.in' + str(pages.find('li', {'class': 's-pagination-item s-pagination-ellipsis'}).find('a')['href'])
        return url
    else:
        return


while True:
    data = getdata(url)
    url = getnextpage(data)
    if not url:
        break
    print(url)