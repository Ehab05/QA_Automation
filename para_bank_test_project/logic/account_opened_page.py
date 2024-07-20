from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from para_bank_test_project.logic.base_app_page import BaseAppPage


class AccountOpenedPage(BaseAppPage):
    PAGE_TITLE = "//div[@id='openAccountResult']/h1[@class='title']"  # XPATH for the page title
    NEW_ACCOUNT_NUMBER = "newAccountId"  # ID for the number of the opened account

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_page_title(self) -> str:
        """
            This function returns the title of the right section of the page
            after successfully opening a new account
        """
        page_title = (WebDriverWait(self._driver, 12).until
                      (EC.visibility_of_element_located((By.XPATH, self.PAGE_TITLE))))
        return page_title.text
