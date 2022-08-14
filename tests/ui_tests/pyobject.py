import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\Users\\gring\\PycharmProjects\\pythonProject\\qa_automation\\tests\\ui_tests\\chromedriver.exe')  # Optional argument, if not specified will search path.


driver.get('https://www.saucedemo.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element(By.NAME, 'user-name')
search_box.send_keys('standard_user')
search_box = driver.find_element(By.NAME, 'password')
search_box.send_keys('secret_sauce')
search_box = driver.find_element(By.NAME, 'login-button')
search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()