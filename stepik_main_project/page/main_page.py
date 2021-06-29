from selenium.webdriver.common.by import By

from stepik_main_project.page.base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.get("http://selenium1py.pythonanywhere.com/")

        self.browser.find_element(By.CSS_SELECTOR, '#login_link').click()
