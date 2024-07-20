from selenium import webdriver
from selenium.webdriver.common.by import By
from the_internet_herokuapp.infra.base_page import BasePage


class DropDownPage(BasePage):
    DROPDOWN = "//select[@id='dropdown']"

    def __init__(self, driver):
        super().__init__(driver)
        driver = webdriver.Chrome()
        driver.get('https://the-internet.herokuapp.com/')
        self._dropdown = driver.find_element(By.ID, self.DROPDOWN)

    def dropdown(self):
        return self._dropdown
