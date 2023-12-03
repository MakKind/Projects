from selenium import webdriver
from selenium.webdriver.common.by import By

# to keep web browser opem
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

# to bypass captcha
chrome_option.add_argument("--user-agent=Defined")

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.amazon.in")
# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(price.text)
# search_bar = driver.find_element(By.NAME, value="field-keywords")
# submit_button = driver.find_element(By.ID, value="nav-search-submit-button")
# print(search_bar.get_attribute("placeholder"))

bug = driver.find_element(By.XPATH, value='//*[@id="navSwmHoliday"]/a')
print(bug.get_attribute("href"))
driver.quit()
