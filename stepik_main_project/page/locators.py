from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')

class LoginPageLocators:
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_FORM = (By.ID, 'login_form')

class ProductPageLocators:
    BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    ORIGINAL_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1)')
    ELEMENT_WITH_COST = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_IN_BASKET = (
        By.CSS_SELECTOR,
        '.alert-success:first-child .alertinner strong'
    )
    ELEMENT_IN_BASKET_WITH_COST = (
        By.CSS_SELECTOR,
        '.alert-info .alertinner strong'
    )
