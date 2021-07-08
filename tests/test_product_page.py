from stepik_main_project.page.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    page_of_product = ProductPage(
        browser,
        'http://selenium1py.pythonanywhere.com/en-gb/catalogue/'
        'the-shellcoders-handbook_209/?promo=newYear')
    page_of_product.open()

    page_of_product.add_to_basket()
    page_of_product.solve_quiz_and_get_code()

    page_of_product.should_be_added_to_busket()
