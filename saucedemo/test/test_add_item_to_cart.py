from saucedemo.infra.browser_wrapper import BrowserWrapper
from saucedemo.logic.cart_page import CartPage
from saucedemo.logic.log_in_page import SwagLabsLogInPage
from saucedemo.logic.main_page import MainPage


class TestMainPage:
    def test_add_item_to_cart(self):
        driver = BrowserWrapper().get_driver()
        login_page = SwagLabsLogInPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        main_page = MainPage(driver)
        main_page.add_item_to_cart('Sauce Labs Bike Light')
        main_page.go_to_cart()
        cart_page = CartPage(driver)
        items_in_cart = cart_page.count_cart_items()
        assert items_in_cart == 1
        driver.quit()
