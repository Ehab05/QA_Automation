import unittest
from para_bank_test_project.infra.browser_wrapper import BrowserWrapper
from para_bank_test_project.infra.config_provider import ConfigProvider
from para_bank_test_project.infra.utils import Utils
from para_bank_test_project.logic.login_page import LoginPage
from para_bank_test_project.logic.register_page import RegisterPage
from para_bank_test_project.logic.successfully_register import SuccessfulRegister
from para_bank_test_project.logic.transfer_complet_page import TransferCompletePage
from para_bank_test_project.logic.transfer_funds_page import TransferFundsPage


class TestTransferFundsPage(unittest.TestCase):

    def setUp(self):
        # Pre conditions
        self._driver = BrowserWrapper().get_driver()
        self._config = ConfigProvider().load_from_file("..//config_parabank.json")
        login_page = LoginPage(self._driver)
        login_page.click_register_button()
        register_page = RegisterPage(self._driver)
        register_page.register_flow_from_config(self._config)
        successfully_register_page = SuccessfulRegister(self._driver)
        successfully_register_page.click_open_new_account_link()
        successfully_register_page.open_new_account_flow(self._config)
        successfully_register_page.click_transfer_funds_link()

    def tearDown(self):
        transfer_complete_page = TransferCompletePage(self._driver)
        transfer_complete_page.click_log_out_button()
        self._driver.quit()

    def test_transfer_funds_with_valid_amount(self):
        """
            Test case: 009
            Verifying the functionality of the funds transfer process for a newly
            registered user by ensuring that a user can successfully transfer funds
            between accounts and receive the appropriate confirmation message.
        """
        # Choosing the data required for the transfer
        transfer_funds_page = TransferFundsPage(self._driver)
        transfer_funds_page.insert_transfer_amount(Utils.generate_amount(self._driver, (100, 200)))
        transfer_funds_page.select_random_account_to_transfer_from()
        transfer_funds_page.select_random_account_to_transfer_to()
        transfer_funds_page.click_transfer_button()
        transfer_complete_page = TransferCompletePage(self._driver)
        # asserting successful message for the transfer
        self.assertTrue(transfer_complete_page.check_title(transfer_complete_page.get_page_title()))

    def test_transfer_funds_with_invalid_amount(self):
        """
            Test case: 010
            Verifying appropriate error message when clicking TRANSFER
            button with invalid amount input
        """

        # Choosing the data required for the transfer with no amount insert
        transfer_funds_page = TransferFundsPage(self._driver)
        transfer_funds_page.insert_transfer_amount(self._config["invalid_transfer_amount"])
        transfer_funds_page.select_random_account_to_transfer_from()
        transfer_funds_page.select_random_account_to_transfer_to()
        transfer_funds_page.click_transfer_button()

        # asserting error message for the missing data
        self.assertIn(self._config["transfer_funds_error_message"], transfer_funds_page.get_error_message())

    def test_transfer_funds_with_empty_amount(self):
        """
            Test case: 011
            Verifying appropriate error message when clicking TRANSFER
            button with no amount input
        """

        # Choosing the data required for the transfer with no amount insert
        transfer_funds_page = TransferFundsPage(self._driver)
        transfer_funds_page.clear_transfer_amount_field()
        transfer_funds_page.select_random_account_to_transfer_from()
        transfer_funds_page.select_random_account_to_transfer_to()
        transfer_funds_page.click_transfer_button()

        # asserting error message for the missing data
        self.assertIn(self._config["transfer_funds_error_message"], transfer_funds_page.get_error_message())
