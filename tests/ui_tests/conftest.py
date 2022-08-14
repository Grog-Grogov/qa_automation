import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome("C:\\Users\\gring\\PycharmProjects\\pythonProject\\qa_automation\\tests\\ui_tests\\chromedriver.exe")
    yield driver
    driver.quit()