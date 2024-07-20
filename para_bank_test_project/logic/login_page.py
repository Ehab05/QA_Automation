from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from para_bank_test_project.logic.base_app_page import BaseAppPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BaseAppPage):
    REGISTER = "Register"  # using link_text instead of XPATH "//a[@href='register.htm']"
    USER_NAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_BUTTON = "//input[@class='button' and @value='Log In']"
    LOGIN_ERROR_MESSAGE = "//p[@class='error']"
    LEFT_PANEL_TITLE = "//div[@id='leftPanel']/h2"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._failed_login_message = "The username and password could not be verified."
        try:
            self._register = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.LINK_TEXT, self.REGISTER)))
            self._user_name_input = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.USER_NAME_INPUT)))
            self._password_input = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.PASSWORD_INPUT)))
            self._login_button = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.LOGIN_BUTTON)))
        except Exception as e:
            self.logger().error(f"Could not locate the elements: {e}")

    def insert_username(self, username: str) -> None:
        self._user_name_input.send_keys(username)
        self.logger().info(f"The user that was inserted: {username}")

    def insert_password(self, password: str) -> None:
        self._password_input.send_keys(password)
        self.logger().info(f"The password that was inserted: {password}")

    def click_login_button(self) -> None:
        self._login_button.click()

    def login_flow(self, username: str, password: str) -> None:
        """
            Login flow includes inserting the username and clicking the login button
            :param username:
            :param password:
            :return: None
        """
        self.insert_username(username)
        self.insert_password(password)
        self.click_login_button()

    def click_register_button(self) -> None:
        self._register.click()

    def get_login_error_message(self):
        """
        When failing to log in, an error message appears this function locate this error and returns the text.
        :return: The error that appears after failed login
        """
        return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located
                                                     ((By.XPATH, self.LOGIN_ERROR_MESSAGE))).text

    def get_login_panel_title(self):
        """
        This function locate the title of the left panel of the login page
        after log out the title should be welcome customer
        :return: The title text of the log in page left panel
        """
        return (WebDriverWait(self._driver, 10).until
                (EC.visibility_of_element_located((By.XPATH, self.LEFT_PANEL_TITLE)))).text
