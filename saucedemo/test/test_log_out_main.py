from saucedemo.infra.browser_wrapper import BrowserWrapper
from saucedemo.logic.log_in_page import SwagLabsLogInPage
from saucedemo.logic.main_page import MainPage


class TestLogOut:
    def test_logout_successfully(self):
        driver = BrowserWrapper().get_driver()
        login_page = SwagLabsLogInPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        main_page = MainPage(driver)
        main_page.click_logout()

