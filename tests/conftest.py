import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en')


@pytest.fixture(scope='function')
def browser(request):
    options = Options()
    custom_language = request.config.getoption('language')
    options.add_experimental_option('prefs',
                                    {'intl.accept_languages': custom_language}
                                    )
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
