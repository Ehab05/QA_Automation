from selenium import webdriver
from selenium.webdriver.common.by import By

from saucedemo.logic.base_page_app import BasePageApp


class MainPage(BasePageApp):
    BACK_PACK = 'add-to-cart-sauce-labs-backpack'
    BIKE_LIGHT = 'add-to-cart-sauce-labs-bike-light'
    ONE_SIE = 'add-to-cart-sauce-labs-onesie'
    FLEECE_JACKET = 'add-to-cart-sauce-labs-fleece-jacket'
    BOLT_TSHIRT = 'add-to-cart-sauce-labs-bolt-t-shirt'
    TSHIRT_RED = 'add-to-cart-test.allthethings()-t-shirt-(red)'

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._back_pack = self._driver.find_element(By.ID, self.BACK_PACK)
        self._bike_light = self._driver.find_element(By.ID, self.BIKE_LIGHT)
        self._one_size = self._driver.find_element(By.ID, self.ONE_SIE)
        self._fleece_jacket = self._driver.find_element(By.ID, self.FLEECE_JACKET)
        self._bolt_tshirt = self._driver.find_element(By.ID, self.BOLT_TSHIRT)
        self._tshirt_red = self._driver.find_element(By.ID, self.TSHIRT_RED)

    def add_item_to_cart(self, item):
        item = item.lower()
        if item == 'sauce labs backpack':
            self._back_pack.click()
        if item == 'sauce labs onesie':
            self._one_size.click()
        if item == 'sauce labs bike light':
            self._bike_light.click()
        if item == 'add to cart sauce labs fleece jacket':
            self._fleece_jacket.click()
        if item == 'add to cart sauce labs bolt t-shirt':
            self._bolt_tshirt.click()
        if item == 'add to cart test.allthethings() t-shirt (red)':
            self._tshirt_red.click()

    def remove_item_from_main(self, item_to_remove):
        item_to_remove = item_to_remove.lower()
        remove_id = None
        if item_to_remove == 'sauce labs backpack':
            remove_id = self.BACK_PACK.replace("add-to-cart", "remove")
        elif item_to_remove == 'sauce labs bike light':
            remove_id = self.BIKE_LIGHT.replace("add-to-cart", "remove")
        elif item_to_remove == 'sauce labs onesie':
            remove_id = self.ONE_SIE.replace("add-to-cart", "remove")
        elif item_to_remove == 'sauce labs fleece jacket':
            remove_id = self.FLEECE_JACKET.replace("add-to-cart", "remove")
        elif item_to_remove == 'sauce labs bolt t-shirt':
            remove_id = self.BOLT_TSHIRT.replace("add-to-cart", "remove")
        elif item_to_remove == 'add to cart test.allthethings() t-shirt (red)':
            remove_id = self.TSHIRT_RED.replace("add-to-cart", "remove")

        if remove_id:
            self._driver.find_element(By.ID, remove_id).click()
        else:
            raise ValueError(f"Item '{item_to_remove}' is not recognized.")
