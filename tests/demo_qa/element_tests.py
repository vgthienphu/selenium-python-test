import time
import unittest
from src.base.base_test import BaseTest
from src.pages.home_page import HomePage

class ElementTest(BaseTest):
    def test_element(self):
        homePage = HomePage(self.driver)

        homePage.scroll_to_bottom_by_script()

        time.sleep(5)

        homePage.click_elements_button()

if __name__ == '__main__':
    unittest.main()





