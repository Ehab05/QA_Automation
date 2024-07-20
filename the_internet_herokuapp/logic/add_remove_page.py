from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from the_internet_herokuapp.infra.base_page import BasePage


class AddRemovePage(BasePage):
    ADD_BUTTON = '//button'
    DELETE_BUTTONS = 'elements'

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._add_button = driver.find_element(By.XPATH, self.ADD_BUTTON)


    def add_element(self):
        add_button = WebDriverWait(self._driver, 10).until(EC.visibility_of(self._add_button))
        add_button.click()

    def number_of_delete_buttons(self):
        return len(self._driver.find_elements(By.ID, self.DELETE_BUTTONS))

    def find_delete_buttons(self):
        self._delete_buttons = self._driver.find_elements(By.ID, self.DELETE_BUTTONS)

    def delete_button(self, button_index):
        # Check if the list is populated
        if self.number_of_delete_buttons():
            self.find_delete_buttons()
        else:
            print("there is no added elements")

        # Ensure the index is within the range of the list
        if button_index < 0 or button_index >= len(self._delete_buttons):
            raise IndexError(f"Button index {button_index} is out of range")

        # Click the button at the specified index
        self._delete_buttons[button_index].click()
