from selenium import webdriver

from saucedemo.infra.browser_wrapper import BrowserWrapper
from saucedemo.logic.cart_page import CartPage
from saucedemo.logic.log_in_page import SwagLabsLogInPage
from saucedemo.logic.main_page import MainPage


class TestCartPage():
    def test_add_2_items_to_cart(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        login_page = SwagLabsLogInPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        main_page = MainPage(driver)
        main_page.add_item_to_cart('Sauce Labs Bike Light')
        main_page.add_item_to_cart('Sauce Labs Onesie')
        main_page.go_to_cart()
        cart_page = CartPage(driver)
        items_in_cart = cart_page.count_cart_items()
        assert items_in_cart == 2

    def test_add_3_items_to_cart_with_1_remove(self):
        driver = BrowserWrapper().get_driver()
        login_page = SwagLabsLogInPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        main_page = MainPage(driver)
        main_page.add_item_to_cart('Sauce Labs Bike Light')
        main_page.add_item_to_cart('Sauce Labs Onesie')
        main_page.add_item_to_cart('add to cart test.allthethings() t-shirt (red)')
        main_page.go_to_cart()
        cart_page = CartPage(driver)
        cart_page.remove_item_from_cart('Sauce Labs Bike Light')
        items_in_cart = cart_page.count_cart_items()
        assert items_in_cart == 2
        driver.quit()
