from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from saucedemo.logic.base_page_app import BasePageApp
from saucedemo.logic.main_page import MainPage


class CartPage(BasePageApp):
    CHECK_OUT = 'checkout'  # ID
    CONTINUE_SHOPPING = 'continue-shopping'  # ID
    BACK_PACK_REMOVE = 'remove-sauce-labs-backpack'
    BIKE_LIGHT_REMOVE = 'remove-sauce-labs-bike-light'
    ONE_SIE_REMOVE = 'remove-sauce-labs-onesie'
    FLEECE_JACKET_REMOVE = 'remove-sauce-labs-fleece-jacket'
    BOLT_TSHIRT_REMOVE = 'remove-sauce-labs-bolt-t-shirt'
    TSHIRT_RED_REMOVE = 'remove-test.allthethings()-t-shirt-(red)'

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._cart_list = self._driver.find_element(By.CLASS_NAME, "cart_list")
        self._cart_items = self._cart_list.find_elements(By.CLASS_NAME, "cart_item")
        self._back_pack_remove = self._driver.find_element(By.ID, self.BACK_PACK_REMOVE)
        self._bike_light_remove = self._driver.find_element(By.ID, self.BIKE_LIGHT_REMOVE)
        self._one_size_remove = self._driver.find_element(By.ID, self.ONE_SIE_REMOVE)
        self._fleece_jacket_remove = self._driver.find_element(By.ID, self.FLEECE_JACKET_REMOVE)
        self._bolt_tshirt_remove = self._driver.find_element(By.ID, self.BOLT_TSHIRT_REMOVE)
        self._tshirt_red_remove = self._driver.find_element(By.ID, self.TSHIRT_RED_REMOVE)

    def count_cart_items(self):
        active_cart_items = [item for item in self._cart_items if
                             "removed_cart_item" not in item.get_attribute("class")]
        return len(active_cart_items)

    def remove_item_from_cart(self, item_to_remove):
        item_to_remove = item_to_remove.lower()
        if item_to_remove == 'sauce labs backpack':
            self._driver.find_element(By.ID, self.BACK_PACK_REMOVE).click()
        elif item_to_remove == 'sauce labs onesie':
            self._driver.find_element(By.ID, self.ONE_SIE_REMOVE).click()
        elif item_to_remove == 'sauce labs bike light':
            self._driver.find_element(By.ID, self.BIKE_LIGHT_REMOVE).click()
        elif item_to_remove == 'add to cart sauce labs fleece jacket':
            self._driver.find_element(By.ID, self.FLEECE_JACKET_REMOVE).click()
        elif item_to_remove == 'add to cart sauce labs bolt t-shirt':
            self._driver.find_element(By.ID, self.BOLT_TSHIRT_REMOVE).click()
        elif item_to_remove == 'add to cart test.allthethings() t-shirt (red)':
            self._driver.find_element(By.ID, self.TSHIRT_RED_REMOVE).click()

        else:
            return None
