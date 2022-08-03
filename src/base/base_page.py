from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from seleniumpagefactory.Pagefactory import PageFactory

class BasePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_bottom_by_script(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_bottom(self):
        html = self.driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)

    def scroll_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()