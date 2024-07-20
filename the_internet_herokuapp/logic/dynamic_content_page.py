from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from the_internet_herokuapp.infra.base_page import BasePage


class DynamicContentPage(BasePage):
    CLICK_DYNAMIC = "//a[@href='/dynamic_content?with_content=static']"
    DYNAMIC_IMAGE = "(//div[@class='large-2 columns'])[3]"
    DYNAMIC_TEXT = "(//div[@class='large-10 columns'])[3]"

    def __init__(self, driver):
        super().__init__(driver)
        self._click_dynamic = driver.find_element(By.XPATH, self.CLICK_DYNAMIC)
        self._dynamic_image = driver.find_element(By.XPATH, self.DYNAMIC_IMAGE)
        self._dynamic_text = driver.find_element(By.XPATH, self.DYNAMIC_TEXT)

    def get_dynamic_image(self):
        return self._dynamic_image

    def get_dynamic_text(self):
        return self._dynamic_text

    def get_dynamic_image_flow(self):
        self._click_dynamic.click()
        WebDriverWait(self._driver, 15).until(EC.visibility_of(self._dynamic_image))
        return self._dynamic_image

    def get_dynamic_text_flow(self):
        self._click_dynamic.click()
        WebDriverWait(self._driver, 15).until(EC.visibility_of(self._dynamic_text))
        return self._dynamic_text
