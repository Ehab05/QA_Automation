from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from youtube.infra.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

from youtube.infra.utils import Utils


class YoutubeHomePage(BasePage):
    SEARCH_BAR_INPUT = "//input[@id='search']"
    SHORTS_ICON = "//yt-formatted-string[contains(text(),'Shorts')]"
    SUBSCRIPTIONS_ICON = "//yt-formatted-string[contains(text(),'Subscriptions')]"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._search_bar_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
            By.XPATH, self.SEARCH_BAR_INPUT)))
        self._shorts_icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
            By.XPATH, self.SHORTS_ICON)))
        self._subscriptions_icon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
            By.XPATH, self.SUBSCRIPTIONS_ICON)))

    def go_to_shorts_page(self):
        try:
            self._shorts_icon.click()
        except Exception as e:
            print(f"Error clicking on the link:{e}")

    def search_for(self, search_input):
        try:
            self._search_bar_input.send_keys(search_input)
            self._search_bar_input.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"Search was not successful: {e}")

    def get_page_title(self, driver, page_title):
        Utils.wait_for_action(driver.title, page_title, 2, 5)
        return driver.title
