from selenium import webdriver
from selenium.webdriver.common.by import By

from the_internet_herokuapp.infra.base_page import BasePage


class CheckBoxes(BasePage):
    CHECKBOX_1 = "//form[@id='checkboxes']/input[1]"
    CHECKBOX_2 = "//form[@id='checkboxes']/input[2]"

    def __init__(self, driver):
        super().__init__(driver)
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/")

    def checkbox(self, checkbox_number):
        return self._driver.find_element(By.XPATH, f"self.CHECKBOX_{checkbox_number}")
