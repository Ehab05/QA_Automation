import logic
from selenium.webdriver.common.by import By
import infra


def test_google_search():
    setup = infra.WebDriverSetup()
    driver = setup.get_driver('chrome')
    try:
        driver.get("http://www.google.com/")
        driver.implicitly_wait(10)
        google_search = logic.SearchGoogle(driver)
        google_search.search_by_text("Python programming")
        check = google_search.check_search_results("Python For Beginners")
        assert check == "Python For Beginners"
        print(f"Yay the test has passed we found : {check}")

    except Exception as e:
        print(f"We didn't find it sorry:{e}")

    driver.quit()
