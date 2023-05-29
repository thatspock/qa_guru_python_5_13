import pytest
from selenium import webdriver
from selene import browser

desktop_sizes = [(1710, 1121), (1470, 956)]
mobile_sizes = [(360, 780), (428, 926)]

browser_sizes = [pytest.param(size, id='desktop') for size in desktop_sizes] + \
                [pytest.param(size, id='mobile') for size in mobile_sizes]


@pytest.fixture(params=browser_sizes)
def web_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[1]
    browser.config.window_width = request.param[0]

    yield browser

    browser.quit()


def test_github_desktop(web_browser, request):
    if 'mobile' in request.node.name:
        pytest.skip('Skipping this test for mobile dimensions')

    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()


def test_github_mobile(web_browser, request):
    if 'desktop' in request.node.name:
        pytest.skip('Skipping this test for desktop dimensions')

    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()
