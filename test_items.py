link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
from selenium.webdriver.common.by import By


def test_user_should_see_appropriate_language_interface(browser):
    browser.get(link)
    item = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert item, "no item"


