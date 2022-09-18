from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches",["enable-logging"])

driver = webdriver.Chrome(options=options)

driver.get('https://v.qq.com/')


titles = driver.find_elements(By.XPATH,'//*[@id="new_vs_hot_today"]/div[2]/div/div/div/a')
time.sleep(4)

for i in titles:
  print(i.text)
