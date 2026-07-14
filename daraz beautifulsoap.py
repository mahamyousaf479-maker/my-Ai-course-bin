#Python program to scrape website 

import requests
from bs4 import BeautifulSoup
import csv

with open('C:\\binb\\Daraz.pk.htm', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html5lib')

smartphone = []

table = soup.find('div', attrs = {'class': '_17mcb'})

for row in table.find_all('div',
                          attrs = { 'class':'Bm3ON'} ):
    smartphones = {}
    smartphones['url'] = row.a['href']
    smartphones['img'] = row.img['src']
    smartphones['discription'] = row.img['alt']
    smartphone.append(smartphones)

filename = 'smart-phonesData-BeautifulSoap.csv'
with open(filename, 'w', newline='' ,encoding='utf-8') as f:
    w = csv.DictWriter(f,['url', 'img', 'discription'])
    w.writeheader()
    for smartphones in smartphone:
        w.writerow(smartphones)