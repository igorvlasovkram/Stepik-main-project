import pytest

from stepik_main_project.page.product_page import ProductPage


@pytest.mark.parametrize('promo',
                         ["?promo=offer0",
                          "?promo=offer1",
                          "?promo=offer2",
                          "?promo=offer3",
                          "?promo=offer4",
                          "?promo=offer5",
                          "?promo=offer6",
                          pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                          "?promo=offer8",
                          "?promo=offer9"]
                         )
def test_guest_can_add_product_to_basket(browser, promo):
    page = ProductPage(
        browser,
        f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        f'{promo}')
    page.open()

    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_added_to_busket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    page.open()

    page.add_to_basket()

    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    page.open()

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

    page.should_be_on_login_page()
