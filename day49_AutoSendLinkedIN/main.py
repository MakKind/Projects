import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
chrome_option.add_argument("--user-agent=Defined")
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("binmainak813@gmail.com")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("#Senjuti13")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Keys.ENTER)
time.sleep(20)
driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button').click()
driver.find_element(By.CSS_SELECTOR, 'footer button').click()
driver.find_element(By.CSS_SELECTOR, 'footer button').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__actionbar button').click()
time.sleep(5)
# driver.quit()

# Note to self: this project is half complete, and I am abandoning it for the time being as i am not finding myself
# motivated to work through it . I will certainly return for you to complete this
