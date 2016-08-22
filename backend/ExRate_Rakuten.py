import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import xlwt
from random import randint
from time import sleep
from datetime import datetime

from bs4 import BeautifulSoup as bs

ask = []
bid = []

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver

driver = init_driver()
url="https://www.rakuten-sec.co.jp/web/market/data/exchange_top.html"
driver.get(url)
time.sleep(10)
html = driver.page_source

soup = bs(html, "html.parser")
table = soup.find("table", {"class":"tbl-data-01"})
# rows = table.find_all("tr")
tbody = table.find("tbody")
rows = tbody.find_all("tr")

for row in rows :
		ask_tag = row.findNext('td')
		bid_tag = ask_tag.findNext('td').string
		ask.append(ask_tag.string)
		bid.append(bid_tag.string)

driver.quit()

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("ForexData")
n = len(ask)
i = 0
while i < n:
        sheet1.write(i+1, 1, ask[i])
        sheet1.write(i+1, 2, bid[i])
        i = i+1

sheet1.write(0, 4,str(datetime.now()))
book.save("FXcalculator.xls")

print 'done'

