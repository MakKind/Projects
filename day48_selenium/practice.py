from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

chrome_option.add_argument("--user-agent=Defined")

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/events/python-events/")
event_title = driver.find_elements(By.CLASS_NAME, value="event-title")
event_date = driver.find_elements(By.CSS_SELECTOR, value='ul li p time')
dict_print = {}
for i in range(len(event_title)):
    dict_print[i] = {'time': event_date[i].text, 'name': event_title[i].text}

print(dict_print)
driver.quit()
