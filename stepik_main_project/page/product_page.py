from stepik_main_project.page.base_page import BasePage
from stepik_main_project.page.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET).click()

    def should_be_added_to_busket(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.ORIGINAL_PRODUCT
        ).text
        product_cost = self.browser.find_element(
            *ProductPageLocators.ELEMENT_WITH_COST
        ).text
        product_name_in_basket = self.browser.find_element(
            *ProductPageLocators.PRODUCT_IN_BASKET
        ).text
        basket_cost = self.browser.find_element(
            *ProductPageLocators.ELEMENT_IN_BASKET_WITH_COST
        ).text

        assert product_name == product_name_in_basket, \
            'Product name is not equal to product name in basket'
        assert product_cost == basket_cost, \
            'Basket cost is not equal to product cost'

    def should_not_be_success_message(self):
        assert self.is_not_element_present \
            (*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_already(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
