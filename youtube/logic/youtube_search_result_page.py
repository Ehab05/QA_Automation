from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from youtube.infra.base_page import BasePage


class YoutubeSearchResultPage(BasePage):
    SEARCH_RESULTS = "//*[@id='video-title']"
    HOME_BUTTON = 'logo'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.SEARCH_RESULTS))
        )
        self._search_results = driver.find_elements(By.XPATH, self.SEARCH_RESULTS)
        self._video_titles = list(map(lambda result: result.get_attribute("title"), self._search_results))
        self._home_button = driver.find_element(By.ID, self.HOME_BUTTON)

    def check_text_in_search_result(self, text):
        WebDriverWait(self._driver, 10)
        filtered_list = list(filter(lambda result: text in result.lower(), self._video_titles))
        return any(filtered_list)

    def click_on_video_title(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_RESULTS))
        )
        if self._search_results:
            self._search_results[1].click()
        else:
            raise IndexError("No search results available to click.")

    def get_video_title(self) -> str:
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.SEARCH_RESULTS)))
        if self._search_results:
            return self._search_results[1].get_attribute("title")
        else:
            raise IndexError("No search results available to retrieve title.")

    def go_to_home(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.HOME_BUTTON)))
        self._home_button.click()

