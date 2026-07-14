#webscrapping amazon using beautifulsoap
import requests
from bs4 import BeautifulSoup
import csv
URL = "https://www.amazon.com/b?_encoding=UTF8&node=21217035011&ref_=cct_cg_SHnav2_2a1&pf_rd_p=12b44fc7-b592-4f55-b8d7-32c20b211ef1&pf_rd_r=9Z4KFSRNJF7N2MG3RRFC"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')

quotes=[]  # a list to store quotes
 
table = soup.find('div', attrs = {'id':'all_items'}) 
for row in table.find_all('div',
                         attrs = {'class':'text-center mb-8'}):
  quote = {}
  quote['theme'] = row.h5.text
  quote['url'] = row.a['href']
  quote['img'] = row.img['src']
  quote['lines'] = row.img['alt'].split(" ")[0]
  quote['author'] = row.img['alt'].split(" ")[1]
  quotes.append(quote)