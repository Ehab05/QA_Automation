from selenium import webdriver
from selenium.webdriver.common.by import By

from the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains as AC


class ContextMenu(BasePage):
    HOTSPOT = 'hot-spot'

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._hotspot = driver.find_element(By.ID, self.HOTSPOT)


