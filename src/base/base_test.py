import unittest
from src.helpers.driver_helper import DriverHelper
from src.enums.test.Browser import Browser

class BaseTest(unittest.TestCase):
    def setUp(self):
        driver_helper = DriverHelper()
        driver_helper.init_driver(Browser.Edge.value, True)
        self.driver = driver_helper.get_current()

        self.driver.get("https://demoqa.com/")

    def tearDown(self):
        self.driver.close()