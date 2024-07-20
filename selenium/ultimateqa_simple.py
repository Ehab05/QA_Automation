import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")

driver.implicitly_wait(10)


def log_in():
    go_to_login_page = driver.find_element(By.XPATH, "//a[contains(text(),'Go to login page')]")
    go_to_login_page.click()
    check_box = driver.find_element(By.ID, "user[remember_me]")
    if check_box.is_selected():
        check_box.click()
    email = driver.find_element(By.NAME, "user[email]")
    email.send_keys("welcomeback@gmail.com")
    password = driver.find_element(By.NAME, "user[password]")
    password.send_keys("123456")
    submit = driver.find_element(By.XPATH, '//button[contains(text(),"Sign in")]')
    submit.click()
    error_message = driver.find_element(By.CLASS_NAME, "form-error__list-item")
    if error_message.text == "Invalid email or password.":
        print(f"Developpes you rock the test passed")


def xpath_check_1():
    button = driver.find_element(By.XPATH, "//button[contains(text(),'Click Me!')]")
    button.click()


def high_light_1():
    text = driver.find_element(By.XPATH, "//span[contains(text() ,'Highlight me')]")
