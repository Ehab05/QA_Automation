from selenium.webdriver.common.by import By

from saucedemo.infra.base_page import BasePage


class BasePageApp(BasePage):
    HEADER_APPLOGO = '//div[contains(text(),"Swag Labs")]'  # XPATH
    MENU = 'react-burger-menu-btn'  # id
    GO_TO_CART = '//*[@id="shopping_cart_container"]/a'
    MENU_ALL_ITEMS = 'inventory_sidebar_link'
    MENU_ABOUT = 'about_sidebar_link'
    MENU_LOGOUT = 'logout_sidebar_link'
    MENU_RESET_APP_STATE = 'reset_sidebar_link'
    EXIT_MENU = 'react-burger-cross-btn'
    FOOTER_TWITTER = '//a[@href="https://twitter.com/saucelabs"]'
    FOOTER_FACEBOOK = '//a[@href="https://www.facebook.com/saucelabs"]'
    FOOTER_LINKEDIN = '//a[@href="https://www.linkedin.com/company/sauce-labs/"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._header_applogo = self._driver.find_element(By.XPATH, self.HEADER_APPLOGO)
        self._menu = self._driver.find_element(By.ID, self.MENU)
        self._go_to_cart = self._driver.find_element(By.XPATH, self.GO_TO_CART)
        self._menu_all_items = self._driver.find_element(By.ID, self.MENU_ALL_ITEMS)
        self._menu_about = self._driver.find_element(By.ID, self.MENU_ABOUT)
        self._menu_logout = self._driver.find_element(By.ID, self.MENU_LOGOUT)
        self._menu_reset_app_state = self._driver.find_element(By.ID, self.MENU_RESET_APP_STATE)
        self._exit_menu = self._driver.find_element(By.ID, self.EXIT_MENU)
        self._footer_twitter = self._driver.find_element(By.XPATH, self.FOOTER_TWITTER)
        self._footer_facebook = self._driver.find_element(By.XPATH, self.FOOTER_FACEBOOK)
        self._footer_linkedin = self._driver.find_element(By.XPATH, self.FOOTER_LINKEDIN)

    def get_app_logo(self):
        return self._header_applogo.text

    def menu(self, menu_link):
        getattr(self, f"self._menu_{menu_link.lower()}.click()")

    def exit_menu(self):
        self._exit_menu.click()

    def go_to_cart(self):
        self._go_to_cart.click()

    def click_twitter(self):
        self._footer_twitter.click()

    def click_facebook(self):
        self._footer_facebook.click()

    def click_linkedin(self):
        self._footer_linkedin.click()

    def click_menu(self):
        self._menu.click()

    def click_logout(self):
        self._menu_logout.click()

    def logout_flow(self):
        self.click_menu()
        self.click_logout()


