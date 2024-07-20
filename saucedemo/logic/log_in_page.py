from selenium import webdriver
from selenium.webdriver.common.by import By

from saucedemo.infra.base_page import BasePage


class SwagLabsLogInPage(BasePage):
    LOGIN_LOGO = '//*[@id="root"]/div/div[1]'  # XPATH
    USER_NAME = 'user-name'  # ID
    PASSWORD = 'password'  # ID
    LOGIN_BUTTON = 'login-button'  # id

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._login_logo = self._driver.find_element(By.XPATH, self.LOGIN_LOGO)
        self._user_name = self._driver.find_element(By.ID, self.USER_NAME)
        self._password = self._driver.find_element(By.ID, self.PASSWORD)
        self._login_button = self._driver.find_element(By.ID, self.LOGIN_BUTTON)

    def insert_user_name(self, username):
        self._user_name.send_keys(username)

    def insert_password(self, password):
        self._password.send_keys(password)

    def click_login_button(self):
        self._login_button.click()

    def login_flow(self, username, password):
        self.insert_user_name(username)
        self.insert_password(password)
        self.click_login_button()

    def get_login_logo(self):
        return self._login_logo.text
