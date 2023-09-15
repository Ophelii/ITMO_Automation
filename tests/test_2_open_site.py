from selenium import webdriver
from selenium.webdriver.common.by import By  # Объект, от которого будем брать атрибуты с типами поиска ( loc и xpass)
from selenium.common.exceptions import NoSuchElementException  # Лог ошибок (чтобы отлавливать ошибки)


def test_site_visit():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")

    # Конструкция ниже отлавливает ошибки. Если ошибка - выполняется след блок кода после except.
    # Иначе говоря, мы ищем элемент, если элемент находится - assert false, если не найден - assert true(тест пройден)
    try:
        driver.find_element(By.CSS_SELECTOR, 'header > a > img')  # header > a > ing - локатор, то с помощью чего мы ищем на странице
    except NoSuchElementException:
        assert False
    assert True

# корневой элемент - <html> (html-тег)
