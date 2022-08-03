from src.base.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def click_elements_button(self):
        self.driver.find_element(By.XPATH, "//h5[text()='Elements']").click()

    def scroll_to_elements_button(self):
        self.scroll_to_element(self.driver.find_element(By.XPATH, "//h5[text()='Elements']"))