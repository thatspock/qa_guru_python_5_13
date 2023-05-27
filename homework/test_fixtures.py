import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(params=[(1710, 1121), (1470, 956)])
def setup_desktop_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[0]
    browser.config.window_weight = request.param[1]
    yield browser
    browser.quit()


@pytest.fixture(params=[(320, 240), (480, 360)])
def setup_mobile_browser(request):
    mobile_emulation = {"deviceMetrics": {"width": request.param[0], "height": request.param[1], "pixelRatio": 3.0}}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser.config.driver_options = chrome_options
    yield browser
    browser.quit()


def test_github_desktop(setup_desktop_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(setup_mobile_browser):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
