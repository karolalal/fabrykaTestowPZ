from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.google.pl')

search_box = driver.find_element(By.NAME, 'q')

search_box.click()
driver.implicitly_wait(10)
search_box.send_keys('python')

search_box.submit()
time.sleep(5)

driver.quit()
