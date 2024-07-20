from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from para_bank_test_project.logic.base_app_page import BaseAppPage


class SuccessfulRegister(BaseAppPage):
    PAGE_TITLE = '//h1[@class="title"]'
    LOGOUT_BUTTON = "//a[@href='logout.htm' and contains(text(),'Log Out')]"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._logout = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.LOGOUT_BUTTON)))

    def get_page_title(self) -> str:
        try:
            page_title = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.PAGE_TITLE)))
            return page_title.text
        except Exception as e:
            self.logger().error(f"Error retrieving page title: {e}")

    def get_successful_welcome_message(self, config):
        return f"Welcome {config["user"]}"

    def logout(self):
        self._logout.click()
