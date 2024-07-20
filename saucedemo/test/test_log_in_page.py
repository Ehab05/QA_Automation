import unittest
from selenium import webdriver

from saucedemo.infra.browser_wrapper import BrowserWrapper
from saucedemo.logic.log_in_page import SwagLabsLogInPage
from saucedemo.logic.main_page import MainPage


class TestLoginPage():

    def test_login_successfully(self):
        driver = BrowserWrapper().get_driver()
        login_page = SwagLabsLogInPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        main_page = MainPage(driver)
        assert main_page.get_app_logo() == "Swag Labs"

        driver.quit()



