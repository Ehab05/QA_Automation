from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from youtube.infra.base_page import BasePage


class VideoPage(BasePage):
    VIDEO_TITLE = "//h1//yt-formatted-string[@class='style-scope ytd-watch-metadata']"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._video_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, self.VIDEO_TITLE)))

    def get_video_title(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((
            By.XPATH, self.VIDEO_TITLE)))
        return self._video_title.text
