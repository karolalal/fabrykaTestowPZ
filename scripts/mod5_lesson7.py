import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://fabrykatestow.pl'
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
            self.driver.quit()

    def test1(self):
            self.driver.get('https://fabrykatestow.cupsell.pl/')
            self.driver.back()
            sleep(2)

    def test2(self):
        self.driver.get('https://fabrykatestow.cupsell.pl/')
        self.driver.back()
        self.driver.forward()
        sleep(2)

    def test3(self):
        window_before = self.driver.window_handles[0]
        self.driver.find_element(By.LINK_TEXT, 'ZAPISZ MNIE NA NEWSLETTER!').click()
        window_after = self.driver.window_handles[1]
        sleep(2)
        self.driver.switch_to.window(window_before)
        sleep(2)
        self.driver.switch_to.window(window_after)
        sleep(2)