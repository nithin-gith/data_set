import time

from selenium import webdriver 
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://codeforces.com/problemset?tags=binary+search")

time.sleep(1)

htmlText = driver.page_source

html = BeautifulSoup(htmlText,'html.parser')


qns_div = html.findAll("td",{"class":"id"})

qns_link = []

# print(qns_div[0].find('a')['href'])

for qn in qns_div:
    print(qn.find("a")['href'])




