from selenium import webdriver


class WebDriverSetup:
    def get_driver(self, browser_name:str):
        # Convert browser_name to lowercase to ensure case insensitivity
        browser_name = browser_name.lower()

        # Check if the browser_name is supported
        if browser_name in ['chrome', 'firefox', 'edge']:
            # Dynamically access the webdriver attribute based on browser_name
            driver_class = getattr(webdriver, browser_name.capitalize())
            return driver_class()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
