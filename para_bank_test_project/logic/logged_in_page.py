from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from para_bank_test_project.logic.base_app_page import BaseAppPage


class LoggedPage(BaseAppPage):
    WELCOME_MESSAGE = "//p[@class='smallText']"  # XPATH os the welcome message after successful login
    LOGOUT_BUTTON = "//a[@href='logout.htm' and contains(text(),'Log Out')]"  # Logout button XPATH

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._welcome_message = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.WELCOME_MESSAGE)))
        self._logout_button = self._driver.find_element(By.XPATH, self.LOGOUT_BUTTON)

    def click_logout_button(self) -> None:
        self._logout_button.click()

    def get_full_name_greeting(self, config):
        """
            This function returns the welcome message in the structure that is displayed
            in the logged in page " Welcome first_name last_name" it is used for verifying
            with the actual title of the logged in page
            :param config:
            :return: Welcome message
        """
        return f"Welcome {config['first_name']} {config['last_name']}"

    def logged_in_welcome_message(self):
        return (WebDriverWait(self._driver, 10).until
                (EC.visibility_of_element_located((By.XPATH, self.WELCOME_MESSAGE))).text)
