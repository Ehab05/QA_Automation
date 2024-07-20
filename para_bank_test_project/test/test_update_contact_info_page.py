import unittest
from para_bank_test_project.infra.browser_wrapper import BrowserWrapper
from para_bank_test_project.infra.config_provider import ConfigProvider
from para_bank_test_project.logic.logged_in_page import LoggedPage
from para_bank_test_project.logic.login_page import LoginPage
from para_bank_test_project.logic.profile_updated_page import ProfileUpdatedPage
from para_bank_test_project.logic.update_contact_info_page import UpdateContactInfoPage


class TestUpdateContactInfoPage(unittest.TestCase):
    def setUp(self):
        # Pre conditions
        self._driver = BrowserWrapper().get_driver()
        self._config = ConfigProvider().load_from_file("..//config_parabank.json")
        login_page = LoginPage(self._driver)
        login_page.login_flow(self._config["user"], self._config["password"])

    def tearDown(self):
        profile_updated_page = ProfileUpdatedPage(self._driver)
        profile_updated_page.click_log_out_button()
        self._driver.quit()

    def test_update_contact_first_name(self):
        """
            Test case: 007
             Verifying successful update of the first name in the update contact info section
        """
        # Initialize login page and navigating to the update contact info page
        logged_page = LoggedPage(self._driver)
        logged_page.click_update_contact_info_link()
        # Updating the first name
        update_profile_page = UpdateContactInfoPage(self._driver)
        update_profile_page.update_profile_info_by_section("first_name", self._config["update_contact_info"])
        update_profile_page.click_update_profile_button()
        profile_updated_page = ProfileUpdatedPage(self._driver)
        # asserting successful message for the update
        self.assertEqual(profile_updated_page.get_page_title(), self._config["update_profile_success_message"])

    def test_update_contact_info_with_first_name_missing(self):
        # Initialize login page and navigating to the update contact info page
        logged_page = LoggedPage(self._driver)
        logged_page.click_update_contact_info_link()
        # Clicking update profile with the first name missing
        update_profile_page = UpdateContactInfoPage(self._driver)
        update_profile_page.update_profile_info_by_section("first_name", "")
        update_profile_page.click_update_profile_button()
        # Asserting error message for the missing first name
        self.assertEqual(update_profile_page.get_first_name_error_message(), self._config["first_name_required_message"])






