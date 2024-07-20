from para_bank_test_project.infra.browser_wrapper import BrowserWrapper
from para_bank_test_project.infra.config_provider import ConfigProvider
from para_bank_test_project.logic.logged_in_page import LoggedPage
from para_bank_test_project.logic.login_page import LoginPage
import unittest


class TestLogoutPage(unittest.TestCase):

    def setUp(self):
        # Pre conditions
        self._driver = BrowserWrapper().get_driver()
        self._config = ConfigProvider.load_from_file('../config_parabank.json')
        login_page = LoginPage(self._driver)
        login_page.login_flow(self._config["user"], self._config["password"])

    def tearDown(self):
        self._driver.quit()

    def test_successful_logout_from_login_page(self):
        """
            Test case: 005
            Verifying successful log out after clicking the logout button in the login page
        """
        # Initialize login page and perform logout
        logged_in_page = LoggedPage(self._driver)
        logged_in_page.click_log_out_button()
        login_page = LoginPage(self._driver)
        # asserting the title of the login page left panel
        self.assertEqual(login_page.get_login_panel_title(), self._config["login_page_left_panel_title"])
