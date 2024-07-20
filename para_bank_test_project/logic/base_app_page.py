from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from para_bank_test_project.infra.base_page import BasePage
from typing import Dict


class BaseAppPage(BasePage):
    # The variables below is the text of the links in the left panel of login page
    OPEN_NEW_ACCOUNT = "Open New Account"
    ACCOUNTS_OVERVIEW = "Accounts Overview"
    TRANSFER_FUNDS = "Transfer Funds"
    BILL_PAY = "Bill Pay"
    FIND_TRANSACTIONS = "Find Transactions"
    UPDATE_CONTACT_INFO = "Update Contact Info"
    REQUEST_LOAN = "Request Loan"
    LOG_OUT = "Log Out"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_page_title(self):
        return self._driver.title

    def click_open_new_account_link(self):
        (WebDriverWait(self._driver, 10).until
         (EC.element_to_be_clickable((By.LINK_TEXT, self.OPEN_NEW_ACCOUNT)))).click()

    def click_transfer_funds_link(self):
        (WebDriverWait(self._driver, 10).until
         (EC.element_to_be_clickable((By.LINK_TEXT, self.TRANSFER_FUNDS)))).click()

    def click_update_contact_info_link(self):
        (WebDriverWait(self._driver, 10).until
         (EC.element_to_be_clickable((By.LINK_TEXT, self.UPDATE_CONTACT_INFO)))).click()

    def click_log_out_button(self):
        (WebDriverWait(self._driver, 10).until
         (EC.element_to_be_clickable((By.LINK_TEXT, self.LOG_OUT)))).click()

    def open_new_account_flow(self, config: Dict):
        """
            This function perform an open account flow by inserting the account
            type from the config file and selecting the first account from the
            dropdown existing account menu.
            :param config:
            :return: None
        """
        # the importing below is for preventing circular import issue between BaseAppPage and OpenNewAccountPage
        from para_bank_test_project.logic.open_new_account_page import OpenNewAccountPage
        open_new_account_page = OpenNewAccountPage(self._driver)
        # Choosing the data required for opening a new account
        open_new_account_page.select_account_type(config["account_type"])
        open_new_account_page.select_existing_account()
        open_new_account_page.click_open_new_account_button()
