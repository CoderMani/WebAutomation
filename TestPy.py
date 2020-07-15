from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")
assert "youtube" in driver.title
time.sleep(5)

driver.find_element_by_id("")
driver.find_element_by_name("")
driver.find_element_by_class("")
driver.find_element_by_text("")
driver.find_element_by_xpath("")



driver.close()
driver.quit()