from stepik_main_project.page.base_page import BasePage
from stepik_main_project.page.login_page import LoginPage
from stepik_main_project.page.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    page = MainPage(
        browser,
        'http://selenium1py.pythonanywhere.com/'
    )
    page.open()

    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


def test_guest_should_see_login_link(browser):
    page = MainPage(
        browser,
        'http://selenium1py.pythonanywhere.com/')
    page.open()

    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasePage(
        browser,
        'http://selenium1py.pythonanywhere.com/'
    )
    page.open()

    page.go_to_basket()

    page.should_has_no_goods_in_basket()
    page.should_has_text_about_empty_basket()
