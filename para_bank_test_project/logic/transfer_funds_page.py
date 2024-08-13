import random


from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from para_bank_test_project.logic.base_app_page import BaseAppPage
from selenium.webdriver.support.select import Select


class TransferFundsPage(BaseAppPage):
    PAGE_TITLE = "//div[@id='showForm']/h1[@class='title']"
    AMOUNT = "amount"
    FROM_ACCOUNT = "fromAccountId"
    TO_ACCOUNT = "toAccountId"
    TRANSFER_BUTTON = "//input[@class='button']"
    ERROR_MESSAGE = "//div[@id='showError']/h1"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._amount = None
        self._from_account = driver.find_element(By.ID, self.FROM_ACCOUNT)
        self._to_account = driver.find_element(By.ID, self.TO_ACCOUNT)
        self._first_option_selected = None

    def insert_transfer_amount(self, transfer_amount):
        self._amount = (WebDriverWait(self._driver, 10).until
                        (EC.visibility_of_element_located((By.ID, self.AMOUNT))))
        self._amount.send_keys(transfer_amount)

    def clear_transfer_amount_field(self):
        self._amount = (WebDriverWait(self._driver, 10).until
                        (EC.visibility_of_element_located((By.ID, self.AMOUNT))))
        self._amount.clear()

    def select_random_account_to_transfer_from(self):
        """
            Selecting a random account number from the transfer from account list
            and assigning the selected account number value to " self._option_selected " for
            excluding it from usage in the transfer process
        """
        try:
            element = (WebDriverWait(self._driver, 10).until
                       (EC.element_to_be_clickable((By.ID, self.FROM_ACCOUNT))))
            select = Select(element)
            options = list(select.options)
            random_option = random.choice(options)
            select.select_by_visible_text(random_option.text)
            self._first_option_selected = [random_option.text, ""]
        except Exception:
            self.logger().error(f"Failed to select the value:{self._from_account}")

    def select_random_account_to_transfer_to(self):
        """
            Selecting a random account number from the transfer to account list
            excluding the selected account number from the transfer from process
        """
        try:
            wait = WebDriverWait(self._driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.ID, self.TO_ACCOUNT)))
            wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//select[@id='{self.TO_ACCOUNT}']/option")))
            select = Select(element)
            options = list(select.options)
            filtered_options = list(filter(lambda option: option.text not in self._first_option_selected, options))
            random_option = random.choice(filtered_options)
            select.select_by_visible_text(random_option.text)
        except Exception:
            self.logger().error(f"Failed to select the value of the transfer to account: {self._to_account}")

    def click_transfer_button(self):
        try:
            (WebDriverWait(self._driver, 10).until
             (EC.element_to_be_clickable((By.XPATH, self.TRANSFER_BUTTON)))).click()
        except Exception:
            self.logger().error("Failed to click the button")

    def get_page_title(self):
        return (WebDriverWait(self._driver, 10).until
                (EC.visibility_of_element_located((By.XPATH, self.PAGE_TITLE)))).text

    def get_error_message(self):
        """
            Returning the error message if the transfer fund process was unsuccessful
            :return: Error message
        """
        message = (WebDriverWait(self._driver, 10).until
                   (EC.visibility_of_element_located((By.XPATH, self.ERROR_MESSAGE))))
        return message.text
