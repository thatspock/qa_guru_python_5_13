import pytest
from selene import browser
from selenium import webdriver

desktop_sizes = [(1710, 1121), (1470, 956)]
mobile_sizes = [(360, 780), (428, 926)]

desktop_only = pytest.mark.parametrize('web_browser', desktop_sizes, indirect=True)
mobile_only = pytest.mark.parametrize('web_browser', mobile_sizes, indirect=True)


@pytest.fixture(params=desktop_sizes + mobile_sizes)
def web_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[1]
    browser.config.window_width = request.param[0]

    yield browser

    browser.quit()


@desktop_only
def test_github_desktop(web_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()

@mobile_only
def test_github_mobile(web_browser):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()