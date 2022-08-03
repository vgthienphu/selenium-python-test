from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("start-maximized")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("https://demoqa.com/")

    def tearDown(self):
        self.driver.close()