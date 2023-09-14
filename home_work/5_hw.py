from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def visit_saucedemo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, "#user-name")
        driver.find_element(By.CSS_SELECTOR, "#password")
        driver.find_element(By.CSS_SELECTOR, "#login-button")
        print("Элементы найдены")
    except NoSuchElementException:
        assert False
    assert True


visit_saucedemo()