from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time,json,random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
with open('data.json') as file:
    data = json.load(file)
for phn in data:
    values = data[phn]
    status = values['status']
    number = phn
driver.get("https://web.whatsapp.com/send?phone={number}&text=Hi}")
driver.maximize_window()
# driver.quit()
