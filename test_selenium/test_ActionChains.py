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
        element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_doubleclick = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        #element_rightclick = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        action = ActionChains(self.driver)
        # action.click(element_click)
        # action.double_click(element_doubleclick)
        try:
            action.click_and_hold(element_rightclick).release()
            print("测试通过")
        except:
            print("测试未通过")

        sleep(1)
        action.perform()


if __name__ == '__main__':
    pytest.main()
