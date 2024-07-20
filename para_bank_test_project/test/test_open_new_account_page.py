import unittest
from para_bank_test_project.infra.browser_wrapper import BrowserWrapper
from para_bank_test_project.infra.config_provider import ConfigProvider
from para_bank_test_project.logic.account_opened_page import AccountOpenedPage
from para_bank_test_project.logic.logged_in_page import LoggedPage
from para_bank_test_project.logic.login_page import LoginPage
from para_bank_test_project.logic.open_new_account_page import OpenNewAccountPage


class TestOpenNewAccountPage(unittest.TestCase):

    def setUp(self):
        # Pre conditions
        self._driver = BrowserWrapper().get_driver()
        self._config = ConfigProvider().load_from_file("..//config_parabank.json")
        login_page = LoginPage(self._driver)
        login_page.login_flow(self._config["user"], self._config["password"])

    def tearDown(self):
        account_opened_page = AccountOpenedPage(self._driver)
        account_opened_page.click_log_out_button()
        self._driver.quit()

    def test_open_new_account_page(self):
        """
            Test case: 006
            Verifying the successful opening of a new account on the logged-in page.
        """
        # Initialize login page and navigating to the open new account page
        logged_page = LoggedPage(self._driver)
        logged_page.click_open_new_account_link()
        open_new_account_page = OpenNewAccountPage(self._driver)
        # Choosing the data required for opening a new account
        open_new_account_page.select_account_type(self._config["account_type"])
        open_new_account_page.select_existing_account()
        open_new_account_page.click_open_new_account_button()
        account_opened_page = AccountOpenedPage(self._driver)
        # Asserting a successful message for opening a new account
        self.assertEqual(account_opened_page.get_page_title(), self._config["open_new_account_success_message"])
