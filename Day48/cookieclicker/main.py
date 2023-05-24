from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path="/home/sushamae/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie=driver.find_element(By.ID, "cookie")

store_items=driver.find_elements(By.CSS_SELECTOR, "#store div")

store_items_id = [item.get_attribute("id") for item in store_items]

timeout= time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_price=[]
        

