from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from youtube.infra.base_page import BasePage


class ShortsPage(BasePage):
    CONTAINER_ID = "shorts-container"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._container_id = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.ID, self.CONTAINER_ID)))

    def get_container_id(self):
        try:
            return self._container_id.get_attribute("id")
        except Exception as e:
            print(f"Error returning the container id:{e}")
