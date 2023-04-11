from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()

common = []
commonprice = []

url7 = "https://www.hamleys.in/toys-by-ages/0-18-months"
g = session.get(url7)

g.html.render(sleep=1,keep_page=True, scrolldown=20)
items = g.html.find('.text-red')


for item in items:
    # price = {
    #     'price' : item.text
    # }
    common.append(item)

df = pd.DataFrame(common).T
df.to_excel(excel_writer = "C:/Users/kusha/OneDrive/Documents/Python/name.xlsx")