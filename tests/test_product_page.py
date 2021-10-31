import pytest
import time

from stepik_main_project.page.login_page import LoginPage
from stepik_main_project.page.main_page import MainPage
from stepik_main_project.page.product_page import ProductPage


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    page.open()

    page.add_to_basket()

    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    page.open()

    page.add_to_basket()

    page.should_not_be_success_message_already()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser,
                       'http://selenium1py.pythonanywhere.com/en-gb/'
                       'catalogue/the-city-and-the-stars_95/')
    page.open()

    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    page.open()

    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_on_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    page.open()

    page.go_to_basket()

    page.should_has_no_goods_in_basket()
    page.should_has_text_about_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        MainPage(browser, 'http://selenium1py.pythonanywhere.com/') \
            .open()
        MainPage(browser, 'http://selenium1py.pythonanywhere.com/') \
            .go_to_login_page()

        new_email = str(time.time()) + "@fakemail.org"
        LoginPage(browser, browser.current_url) \
            .register_new_user(new_email, '1a2b3c4d5e6f7g8h9i0')
        LoginPage(browser, browser.current_url) \
            .should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(
            browser,
            'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        page.open()

        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(
            browser,
            'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        page.open()

        page.add_to_basket()

        page.should_be_added_to_busket()
