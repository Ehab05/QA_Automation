import unittest
from para_bank_test_project.infra.browser_wrapper import BrowserWrapper
from para_bank_test_project.infra.config_provider import ConfigProvider
from para_bank_test_project.infra.utils import Utils
from para_bank_test_project.logic.login_page import LoginPage
from para_bank_test_project.logic.register_page import RegisterPage
from para_bank_test_project.logic.successfully_register import SuccessfulRegister


class TestRegisterPage(unittest.TestCase):

    def setUp(self):
        # Pre conditions
        self._driver = BrowserWrapper().get_driver()
        self._config = ConfigProvider.load_from_file('../config_parabank.json')

    def tearDown(self):
        self._driver.quit()

    def test_register_new_user_with_valid_input(self):
        """
        Test case: 001
        Test the registration of a new user using data from the config_parabank.json file with
        valid username and password.
        """
        # Initialize main page and navigate to the registration page
        login_page = LoginPage(self._driver)
        login_page.click_register_button()

        # Initialize the register page and perform the registration flow
        register_page = RegisterPage(self._driver)
        register_page.insert_first_name(self._config["first_name"])
        register_page.insert_last_name(self._config["last_name"])
        register_page.insert_address(self._config["address"])
        register_page.insert_city(self._config["city"])
        register_page.insert_state(self._config["state"])
        register_page.insert_zip_code(self._config["zip_code"])
        register_page.insert_phone(self._config["phone"])
        register_page.insert_ssn(self._config["ssn"])
        register_page.insert_user_name(Utils.generate_username(self._driver, 5), self._config)
        register_page.insert_password(Utils.generate_passwrod(self._driver, 8), self._config)
        register_page.insert_confirm_password(self._config["password"])
        register_page.click_register_button()

        # Verify the registration was successful by checking the page title
        successfully_register_page = SuccessfulRegister(self._driver)

        # Assert that the page title is as expected
        self.assertEqual(successfully_register_page.get_page_title(),
                         successfully_register_page.get_successful_welcome_message(self._config))

        successfully_register_page.logout()

    def test_register_new_user_with_password_mismatch(self):
        """
        Test case: 002
        Test the registration of a new user using data from the config_parabank.json file with
        valid username and invalid password.
        """
        # Initialize main page and navigate to the registration page
        login_page = LoginPage(self._driver)
        login_page.click_register_button()

        # Initialize the register page and perform the registration flow
        register_page = RegisterPage(self._driver)
        register_page.insert_first_name(self._config["first_name"])
        register_page.insert_last_name(self._config["last_name"])
        register_page.insert_address(self._config["address"])
        register_page.insert_city(self._config["city"])
        register_page.insert_state(self._config["state"])
        register_page.insert_zip_code(self._config["zip_code"])
        register_page.insert_phone(self._config["phone"])
        register_page.insert_ssn(self._config["ssn"])
        register_page.insert_user_name(Utils.generate_username(self._driver, 5), self._config)
        register_page.insert_password(Utils.generate_passwrod(self._driver, 8), self._config)
        register_page.insert_confirm_password(Utils.scramble_password(self._driver, self._config["password"]))
        register_page.click_register_button()
        self.assertEqual(register_page.get_password_mismatch_message(), self._config["password_mismatch_message"])
