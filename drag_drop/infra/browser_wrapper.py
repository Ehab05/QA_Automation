import os

from selenium import webdriver
from saucedemo.infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), 'config_youtube.json')
        self._driver = None
        self.config = ConfigProvider.load_from_file(config_path)
        print("Test Start")

    def get_driver(self):
        url = self.config.get("url")
        if not url:
            raise ValueError("URL not found in the configuration.")

        if self.config["browser"] == "Chrome":
            self._driver = webdriver.Chrome()
        elif self.config["browser"] == "FireFox":
            self._driver = webdriver.Firefox()
        elif self.config["browser"] == "Edge":
            self._driver = webdriver.Edge()

        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver
