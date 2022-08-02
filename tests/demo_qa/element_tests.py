from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import unittest
from src.base.base_test import BaseTest

class ElementTest(BaseTest):
    def test_element(self):
        # actions = ActionChains(driver)
        # actions.move_to_element(driver.find_element(By.XPATH, "//h5[text()='Elements']")).perform()

        # html = driver.find_element(By.TAG_NAME, 'html')
        # html.send_keys(Keys.END)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(5)

        self.driver.find_element(By.XPATH, "//h5[text()='Elements']").click()

if __name__ == '__main__':
    unittest.main()





