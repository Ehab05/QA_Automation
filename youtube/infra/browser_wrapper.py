from selenium import webdriver
from saucedemo.infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self.config = ConfigProvider.load_from_file('../config_youtube.json')
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
        else:
            print(f"{self.config} is not supported")

        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver
