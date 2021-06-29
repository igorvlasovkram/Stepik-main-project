from stepik_main_project.page.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/')
    page.go_to_login_page()
