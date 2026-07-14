#webscrape amazon using selenuim
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
URL = 'https://www.amazon.com/b?_encoding=UTF8&node=21217035011&ref_=cct_cg_SHnav2_2a1&pf_rd_p=12b44fc7-b592-4f55-b8d7-32c20b211ef1&pf_rd_r=9Z4KFSRNJF7N2MG3RRFC'

cService = webdriver.ChromeService(executable_path='C:\\Users\\win\\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe') # '/Users/bpfalz/Downloads/chromedriver' for my macbook
driver = webdriver.Chrome(service=cService)

driver.get(URL)
qouestList=[]
qoutesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 'text-center mb-8')]")
for p in range(len(qoutesDiv) -1):
    quote = {}
    innerImg = qoutesDiv[p+1].find_element(By.TAG_NAME, "img")
    innera = qoutesDiv[p+1].find_element(By.TAG_NAME, "a")
    quote["img"] =innerImg.get_attribute('src') 
    quote["lines"] =innerImg.get_attribute('alt') 
    quote['url'] = innera.get_attribute('href')
    qouestList.append(quote)

filename = 'Amazon.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['url','img','lines','author'])
    w.writeheader()
    for quote in qouestList:
        w.writerow(quote)

driver.close()