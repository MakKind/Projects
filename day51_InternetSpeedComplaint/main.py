import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True, )
chrome_option.add_argument("--user-agent=Defined")
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://fast.com")
time.sleep(15)
download = driver.find_element(By.CSS_SELECTOR, '.speed-results-container').text
driver.find_element(By.XPATH, '//*[@id="show-more-details-link"]').click()
time.sleep(10)
upload = driver.find_element(By.XPATH, '//*[@id="upload-value"]').text
driver.quit()

msg = f"Hey #BSNL why my Download Speed= {download} Mbps \nUpload Speed= {upload} Mbps, when I pay for 30 Mbps up and 10 Mbps down?"
if float(upload) < 50 or float(download) < 20:
    driver.get("https://twitter.com/")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys("binmainak813@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys("@BinMainak")
    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys("08/08/1996")
    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span').send_keys(msg)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span').click()
else:
    print(f"The speed is good. \nDownload Speed= {download} Mbps \nUpload Speed= {upload} Mbps")
driver.quit()
