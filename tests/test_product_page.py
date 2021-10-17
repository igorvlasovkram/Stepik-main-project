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
    page_of_product = ProductPage(
        browser,
        f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        f'{promo}')
    page_of_product.open()

    page_of_product.add_to_basket()
    page_of_product.solve_quiz_and_get_code()

    page_of_product.should_be_added_to_busket()
