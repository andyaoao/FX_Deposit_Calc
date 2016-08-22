import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

from bs4 import BeautifulSoup as bs
# import urllib2

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver

driver = init_driver()
interest_url = 'http://www.rakuten-bank.co.jp/assets/forexdep/rate.html'
driver.get(interest_url)
time.sleep(10)
interest_html = driver.page_source

interest_soup = bs(interest_html, "html.parser")

for_rows = interest_soup.findAll("tr", {"class":"even"})
yen_rows = interest_soup.findAll("tr", {"class":"even-02"})

for for_row in for_rows:
    one = for_row.find("em")
    two = one.findNext("em")
    three = two.findNext("em")
    four = three.findNext("em")
    five = four.findNext("em")
    six = five.findNext("em")
    seven = six.findNext("em")

driver.quit()


print seven


