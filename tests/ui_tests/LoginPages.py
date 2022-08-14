from BaseApp import BasePage
from selenium.webdriver.common.by import By


class LoginLocators:
    LOCATOR_LOGIN_FIELD = (By.NAME, 'user-name')
    LOCATOR_PASSWORD_BUTTON = (By.NAME, 'password')
    LOCATOR_BUTTON = (By.NAME, 'login-button')


class LoginHelper(BasePage):

    def enter_login(self, login):
        login_field = self.find_element(LoginLocators.LOCATOR_LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(login)
        return login_field

    def enter_password(self, password):
        password_field = self.find_element(LoginLocators.LOCATOR_PASSWORD_BUTTON)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def enter_button(self,):
        button_field = self.find_element(LoginLocators.LOCATOR_BUTTON)
        button_field.click()
        return button_field
