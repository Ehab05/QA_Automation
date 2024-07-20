from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

from the_internet_herokuapp.infra.base_page import BasePage


class BrokenImagesPage(BasePage):
    IMAGES = "//div[@class='example']"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._images = driver.find_elements(By.CLASS_NAME, self.IMAGES)

    def check_image_if_broken(self):
        for img in self._images:
            img_src = img.get_attribute('src')

            # Make an HTTP request to the image's URL
            response = requests.get(img_src)

            if response.status_code != 200:
                print(f"The image with src '{img_src}' is broken.")
            else:
                print(f"The image with src '{img_src}' is loaded successfully.")
