import pytest
from selene import browser
from selenium import webdriver

desktop_sizes = [(1710, 1121), (1470, 956)]
mobile_sizes = [(360, 780), (428, 926)]


@pytest.fixture(params=desktop_sizes)
def setup_desktop_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield browser

    browser.quit()


@pytest.fixture(params=mobile_sizes)
def setup_mobile_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield browser

    browser.quit()


def test_github_desktop(setup_desktop_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(setup_mobile_browser):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
