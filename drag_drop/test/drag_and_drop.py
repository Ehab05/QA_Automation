from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from drag_drop.infra.browser_wrapper import BrowserWrapper


def drag_and_drop():
    driver = BrowserWrapper().get_driver()
    source_element = driver.find_element(By.ID, 'card47')
    target_element = driver.find_element(By.ID, "foun3")
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()
    driver.quit()
