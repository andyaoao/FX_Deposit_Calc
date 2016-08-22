import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup as bs
import urllib2

import xlwt
import xlrd
import os.path
from openpyxl import load_workbook

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver

driver = init_driver()
url="http://jp.investing.com/currencies/usd-jpy-forward-rates"
driver.get(url)
html = driver.page_source

name = []
ask = []
bid = []

soup = bs(html, "html.parser")
table = soup.find("table", {"id":"curr_table"})
tbody = table.find("tbody")
rows = tbody.find_all("tr")
time.sleep(5)

for row in rows :
        name_tag = row.find('td', {'class':["bold","left"]})
        bid_tag = name_tag.findNext('td')
        ask_tag = bid_tag.findNext('td')
        name.append(name_tag.string)
        ask.append(ask_tag.string)
        bid.append(bid_tag.string)
        print name_tag.string
        print ask_tag.string
        print bid_tag.string


n = len(ask)

driver.quit()


print 'Futures done'