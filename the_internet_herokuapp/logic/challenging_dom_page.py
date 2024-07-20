from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from the_internet_herokuapp.infra.base_page import BasePage


class ChallengingDomPage(BasePage):
    BUTTON = "//a[@class='button']"
    BUTTON_ALERT = "//a[@class='button alert']"
    BUTTON_SUCCESS = "//a[@class='button success']"
    CANVAS = 'canvas'
    DYNAMIC_BUTTONS = ("//a[contains(text(),'bar') or contains(text(),'foo') or contains(text(),'baz') or contains("
                       "text(),'qux')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._button = driver.find_element(By.XPATH, self.BUTTON)
        self._button_alert = driver.find_element(By.XPATH, self.BUTTON_ALERT)
        self._button_success = driver.find_element(By.XPATH, self.BUTTON_SUCCESS)
        self._canvas = driver.find_element(By.ID, self.CANVAS)

    def get_button(self):
        return self._button

    def get_dynamic_button(self, button):
        actions = AC(self._driver)
        actions.move_to_element(button).click(button).perform()
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.DYNAMIC_BUTTONS)))

