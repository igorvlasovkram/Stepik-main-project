from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    VIEW_BASKET = (By.CSS_SELECTOR, '.btn-group [class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    ITEMS = (By.CLASS_NAME, '.basket-items')
    MESSAGE_ABOUT_EMPTY_BASKET = (By.ID, 'content_inner')

class LoginPageLocators:
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD = (By.ID, 'id_registration-password1')
    CONFIRM_REGISTRATION_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')

class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')

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
