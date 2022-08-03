from src.base.base_page import BasePage

class HomePage(BasePage):
    locators = {
        'elements_button': ('XPATH', "//h5[text()='Elements']")
    }

    def click_elements_button(self):
        self.elements_button.click()

    def scroll_to_elements_button(self):
        self.scroll_to_element(self.elements_button)