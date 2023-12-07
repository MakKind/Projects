import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True, )
chrome_option.add_argument("--user-agent=Defined")
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://tinder.com")
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="q488047873"]/div/div[2]/div/div/div[1]/div[2]/button').click() # Dismiss Trackers
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="q488047873"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click() #Click Login
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="q-1240333203"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button').click() #Click More options
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="q-1240333203"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]/div/div').click() # Log in by phoen number click
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="q-1240333203"]/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/input').send_keys("7005341852") # Enter number
driver.find_element(By.XPATH, '//*[@id="q-1240333203"]/main/div/div[1]/div/div[3]/button').click() # Click continue # Sometime it will not send OTP, Rerurn after 5 min
time.sleep(20)  # Time to insert the OTP
driver.find_element(By.XPATH, '//*[@id="q-1240333203"]/main/div/div[1]/div/div[4]/button').click() # Click Continue
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="q-1240333203"]/main/div/div/div[1]/div/div[2]/button').click() #gmail verify
time.sleep(20)  # Time to insert the OTP
driver.find_element(By.XPATH, '//*[@id="q-1240333203"]/main/div/div/div[1]/div/div[2]/div[2]/button').click()# Click Continue
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="q-1240333203"]/main/div/div/div/div[3]/button[1]').click() # Allow location
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="q-1240333203"]/main/div/div/div/div[3]/button[2]').click() # Not interested in notifications
time.sleep(20)
i = 0
driver.find_element(By.XPATH, '//*[@id="q488047873"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button').click() #reject
while i < 5:
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="q488047873"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button').click() #reject
    i += 1
driver.quit()
