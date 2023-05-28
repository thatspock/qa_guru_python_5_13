import pytest
from selene import browser
from selenium import webdriver

desktop_only = pytest.mark.parametrize('web_browser', [(1710, 1121), (1470, 956)], indirect=True)
mobile_only = pytest.mark.parametrize('web_browser', [(320, 240), (480, 360)], indirect=True)


@pytest.fixture(params=[(1710, 1121), (1470, 956), (320, 240), (480, 360)])
def web_browser(request):
    chrome_options = webdriver.ChromeOptions()

    if request.param[0] < 800:
        mobile_emulation = {"deviceMetrics": {"width": request.param[0], "height": request.param[1], "pixelRatio": 3.0}}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    else:
        browser.config.window_height = request.param[1]
        browser.config.window_width = request.param[0]

    browser.config.driver_options = chrome_options

    yield browser

    browser.quit()


@desktop_only
def test_github_desktop(web_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


@mobile_only
def test_github_mobile(web_browser):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
