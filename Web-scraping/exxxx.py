from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()

common = []
commonprice = []

#0-18 Months
url1 = "https://www.hamleys.in/toys-by-ages/0-18-months"
a = session.get(url1)

a.html.render(sleep=1,keep_page=True, scrolldown=30)
items = a.html.find('.poppins-semi-bold')
for item in items:
    common.append(item.text)

#price
a.html.render(sleep=1,keep_page=True, scrolldown=30)
items2 = a.html.find('.text-red')
for item in items2:
    commonprice.append(item.text)

#18-36 Months
url2 = "https://www.hamleys.in/toys-by-ages/18-36-months"

b = session.get(url2)
b.html.render(sleep=1,keep_page=True, scrolldown=30)
items3 = b.html.find('.poppins-semi-bold')
for item in items3:
    common.append(item.text)

#price
b.html.render(sleep=1,keep_page=True, scrolldown=30)
items4 = b.html.find('.text-red')
for item in items4:
    commonprice.append(item.text)

#3-5 Years
url3 = "https://www.hamleys.in/toys-by-ages/3-5-years"

c = session.get(url3)
c.html.render(sleep=1,keep_page=True, scrolldown=30)
items5 = c.html.find('.poppins-semi-bold')

for item in items5:
    common.append(item.text)

#price
c.html.render(sleep=1,keep_page=True, scrolldown=30)
items6 = c.html.find('.text-red')
for item in items6:
    commonprice.append(item.text)


#5-7 Years
url4 = "https://www.hamleys.in/toys-by-ages/5-7-years"

d = session.get(url4)
d.html.render(sleep=1,keep_page=True, scrolldown=30)
items7 = d.html.find('.poppins-semi-bold')
for item in items7:
    common.append(item.text)

#price
d.html.render(sleep=1,keep_page=True, scrolldown=30)
items8 = d.html.find('.text-red')
for item in items8:
    commonprice.append(item.text)

#9-12 Years
url5 = "https://www.hamleys.in/toys-by-ages/9-12-years"

e = session.get(url5)
e.html.render(sleep=1,keep_page=True, scrolldown=30)
items9 = e.html.find('.poppins-semi-bold')

for item in items9:
    common.append(item.text)

#price
e.html.render(sleep=1,keep_page=True, scrolldown=30)
items10 = e.html.find('.text-red')
for item in items10:
    commonprice.append(item.text)


#12+ Years
url6 = "https://www.hamleys.in/toys-by-ages/older-than-12-years"

f = session.get(url6)
f.html.render(sleep=1,keep_page=True, scrolldown=30)
items11 = f.html.find('.poppins-semi-bold')
for item in items11:
    common.append(item.text)

#price
f.html.render(sleep=1,keep_page=True, scrolldown=30)
items12 = f.html.find('.text-red')
for item in items12:
    commonprice.append(item.text)

print(len(common))
print(len(commonprice))

df = pd.DataFrame(common).T
df.to_excel(excel_writer = "C:/Users/kusha/OneDrive/Documents/Python/name.xlsx")
df2 = pd.DataFrame(commonprice).T
df2.to_excel(excel_writer = "C:/Users/kusha/OneDrive/Documents/Python/price.xlsx")