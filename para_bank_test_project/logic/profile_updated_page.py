from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from para_bank_test_project.logic.base_app_page import BaseAppPage


class ProfileUpdatedPage(BaseAppPage):
    PAGE_TITLE = "//div[@id='updateProfileResult']/h1"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def reload_page(self):
        self._driver.relaod()

    def get_page_title(self):
        page_title = (WebDriverWait(self._driver, 10).until
                      (EC.visibility_of_element_located((By.XPATH, self.PAGE_TITLE))))
        return page_title.text
