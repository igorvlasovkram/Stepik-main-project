import time

from selenium.webdriver.common.by import By


def test_presence_of_button_add_to_basket(browser):
    browser.get(
        'http://selenium1py.pythonanywhere.com/catalogue/'
        'coders-at-work_207/'
    )
    time.sleep(10)

    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')

    assert len(button) == 1
