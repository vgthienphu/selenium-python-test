from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from src.enums.test.Browser import Browser

class DriverHelper:
    __driver = None

    def init_driver(self, browser):
        match browser:
            case Browser.Firefox.value:
                options = FirefoxOptions()
                service = FirefoxService(GeckoDriverManager().install())
                self.__driver = webdriver.Firefox(service=service, options=options)

            case Browser.Edge.value:
                options = EdgeOptions()
                options.add_argument("start-maximized")
                service = EdgeService(EdgeChromiumDriverManager().install())
                self.__driver = webdriver.Edge(service=service, options=options)

            case _:
                options = ChromeOptions()
                options.add_argument("start-maximized")
                service = ChromeService(ChromeDriverManager().install())
                self.__driver = webdriver.Chrome(service=service, options=options)

    def get_current(self):
        return self.__driver