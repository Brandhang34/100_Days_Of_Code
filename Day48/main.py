from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path="/home/sushamae/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar)

# logo = driver.find_element(By.CLASS_NAME,"python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# xpath=driver.find_element(By.XPATH, "/html/body/div/footer/div[2]/div/ul/li[3]/a")
# print(xpath.text)


event_names_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

event_dates_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

dict = {}
for i in range (0,len(event_names_list)):
    event={}
    event["time"] = event_dates_list[i].get_attribute("datetime")[:10]
    event["name"] = event_names_list[i].text[6:]
    dict[f"{i}"] = event

print(dict)





driver.close()
