from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


class TestActiongChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
    def teardown(self):
        self.driver.quit()
    def test_action_chains(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        sleep(2)
        element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_doubleclick = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        element_rightclick = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        action = ActionChains(self.driver)
        action.click(element_click)
        # sleep(3)
        # action.double_click(element_doubleclick)
        # sleep(3)
        # action.right_clich(element_rightclick)
        sleep(3)
        action.perform()
if __name__ == '__main__':
    pytest.main()