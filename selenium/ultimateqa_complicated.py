from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ultimateqa.com/complicated-page")

driver.implicitly_wait(10)


def solve_equ(equ_num):
    equ = driver.find_element(By.XPATH, f"//div[@id='et_pb_contact_form_{equ_num}']//span")
    sum_num = equ.text.split()
    result = int(sum_num[0]) + int(sum_num[2])
    answer = driver.find_element(By.NAME, f"et_pb_contact_captcha_{equ_num}")
    answer.send_keys(str(result))
    print(result)


solve_equ(0)
