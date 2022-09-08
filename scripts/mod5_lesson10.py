import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://simpletestsite.fabrykatestow.pl/'
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
            self.driver.quit()

    def test1(self):
        self.driver.find_element(By.ID, 'checkbox-header').click()
        sleep(2)
        checkbox = self.driver.find_element(By.XPATH, "//div[@id='checkbox-content']//input[2]")
        checkbox.click()
        sleep(2)
        checkbox.screenshot('.\\screenshot_checkbox.png')
        self.driver.save_screenshot('.\\screenshot.png')





