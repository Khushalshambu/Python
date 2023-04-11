from requests_html import HTMLSession
import pandas as pd
from numpy import product
import requests
from bs4 import BeautifulSoup

session = HTMLSession()

common = []
commonprice = []
for x in range(1,8):
    r = requests.get(f"http://khilonewala.in/catalogue.php?city=hyderabadserilingampally&cat=All&pageNo={}")
    soup = BeautifulSoup(r.content,'lxml')
    