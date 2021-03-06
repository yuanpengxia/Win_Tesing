from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        #self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('霍格沃兹学院')
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '#su').click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,'#s_tab a:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR,'#s_tab a:nth-last-child(3)').click()
        sleep(5)