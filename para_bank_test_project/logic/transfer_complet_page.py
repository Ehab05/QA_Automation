import unittest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from para_bank_test_project.logic.base_app_page import BaseAppPage


class TransferCompletePage(BaseAppPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    PAGE_TITLE = "//div[@id='showResult']/h1[@class='title']"

    def get_page_title(self):
        page_title = (WebDriverWait(self._driver, 10).until
                      (EC.visibility_of_element_located((By.XPATH, self.PAGE_TITLE))))
        return page_title.text

    def check_title(self, title):
        self.logger().info(f"The title after clicking transfer button is:{title}")
        if title == "Transfer Complete!":
            return True
        else:
            return False
