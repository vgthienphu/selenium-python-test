from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demoqa.com/")

#actions = ActionChains(driver)
#actions.move_to_element(driver.find_element(By.XPATH, "//h5[text()='Elements']")).perform()

#html = driver.find_element(By.TAG_NAME, 'html')
#html.send_keys(Keys.END)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(5)

driver.find_element(By.XPATH, "//h5[text()='Elements']").click()

driver.close()