import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from para_bank_test_project.infra.utils import Utils
from para_bank_test_project.logic.base_app_page import BaseAppPage


class OpenNewAccountPage(BaseAppPage):
    ACCOUNT_TYPE = "//div[@id='openAccountForm']/form/select[@id='type']"
    FROM_ACCOUNT = "//select[@id='fromAccountId']"
    OPEN_NEW_ACCOUNT_BUTTON = "//input[@type='button']"
    ACCOUNT_OPENED_TITLE = "//div[@id='openAccountResult']/h1[@class='title']"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._driver = driver
        self._account_type = (WebDriverWait(driver, 10).until
                              (EC.visibility_of_element_located((By.XPATH, self.ACCOUNT_TYPE))))

    def select_account_type(self, account_type):
        select = Select(self._account_type)
        account_type = account_type.upper()
        select.select_by_visible_text(account_type)
        self.logger().info(f"The account type that was selected is:{account_type}")

    def select_existing_account(self):
        """
            This function select the first account from the account dropdown list in the open new account page
            the selection made by index(0) which is the first option of the select list
        """
        try:
            element = (WebDriverWait(self._driver, 12).until
                       (EC.presence_of_element_located((By.XPATH, self.FROM_ACCOUNT))))
            select = Select(element)
            time.sleep(1)
            select.select_by_value(select.first_selected_option.text)

        except Exception as e:
            self.logger().error(f"An error occurred while selecting an existing account:{e}")

    def click_open_new_account_button(self):

        action = Utils.wait_for_action(self._driver.find_element(By.XPATH, self.OPEN_NEW_ACCOUNT_BUTTON), 2, 5)
        element = self._driver.find_element(By.XPATH, self.OPEN_NEW_ACCOUNT_BUTTON)
        if action:
            try:
                element.click()
            except Exception as e:
                self.logger().error(f"Failed to click the button: {e}")
