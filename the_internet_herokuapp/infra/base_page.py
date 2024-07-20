from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    HEAD = '//h3'

    def __init__(self, driver):
        self._driver = driver
        self._head = driver.find_element(By.XPATH, self.HEAD)
        WebDriverWait(self._driver, 10).until(EC.visibility_of(self._head))

    def page_head(self):
        return self._head
