import unittest
from para_bank_test_project.infra.browser_wrapper import BrowserWrapper
from para_bank_test_project.infra.config_provider import ConfigProvider
from para_bank_test_project.infra.utils import Utils
from para_bank_test_project.logic.logged_in_page import LoggedPage
from para_bank_test_project.logic.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        # Pre conditions
        self._driver = BrowserWrapper().get_driver()
        self._config = ConfigProvider.load_from_file('../config_parabank.json')

    def tearDown(self):
        self._driver.quit()

    def test_login_with_registered_user_and_valid_password(self):
        """
        Test case: 003
        Verifying successful log in with registered user and valid password
        """
        # Initialize login page and perform the login flow
        login_page = LoginPage(self._driver)
        # starting the login flow using the user and password from the registration
        login_page.insert_username(self._config["user"])
        login_page.insert_password(self._config["password"])
        login_page.click_login_button()
        logged_in_page = LoggedPage(self._driver)

        # asserting that the welcome message in the successful login page as expected
        self.assertEqual(logged_in_page.get_full_name_greeting(self._config),
                         logged_in_page.logged_in_welcome_message())

    def test_login_with_registered_user_and_invalid_password(self):
        """
         Test case: 004
         Verifying successful error message with logging in with registered
         user and invalid password
        """
        # Initialize login page and perform the login flow
        login_page = LoginPage(self._driver)
        # starting the login flow using the user and password from the registration
        login_page.insert_username(self._config["user"])
        login_page.insert_password(Utils.scramble_password(self._driver, self._config["password"]))
        login_page.click_login_button()
        self.assertEqual(login_page.get_login_error_message(), login_page._failed_login_message)


