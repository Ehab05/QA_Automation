from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from youtube.infra.base_page import BasePage


class YoutubeNoResultsPage(BasePage):
    NO_RESULTS_FOUND = "//div[@class='promo-title style-scope ytd-background-promo-renderer']"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.NO_RESULTS_FOUND)))
        self._no_results_found = driver.find_element(By.XPATH, self.NO_RESULTS_FOUND)

    def no_result_found(self):
        return self._no_results_found.text

