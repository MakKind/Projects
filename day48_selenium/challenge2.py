from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True, )
chrome_option.add_argument("--user-agent=Defined")
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
print(article_count.text)
# article_count.click()
# driver.find_element(By.LINK_TEXT, value='anyone can edit').click() # click on an element by text in link
search = driver.find_element(By.NAME, value='search')
search.send_keys("Bind community")
search.send_keys(Keys.ENTER)
# driver.find_element(By.CSS_SELECTOR, value='#searchform button').click()

driver.quit()
