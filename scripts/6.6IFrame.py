from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://simpletestsite.fabrykatestow.pl/')

driver.maximize_window()

iframe = driver.find_element(By.XPATH, "//div[@id='iframe-header']")
iframe.click()

driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))

driver.find_element(By.ID, 'simpleButton1').click()

htmlelement= driver.find_element(By.TAG_NAME, 'html')

#Scrolls down to the bottom of the page
htmlelement.send_keys(Keys.END)

sleep(2)

driver.save_screenshot('C:/Users/KAROLINKA/PycharmProjects/fabrykaTestowPZ/screenshots/screenIframe.png')

driver.quit()



