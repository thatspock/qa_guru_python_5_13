import pytest
from selene import browser

desktop_only = pytest.mark.parametrize('web_browser', [(1710, 1121), (1470, 956)], indirect=True)
mobile_only = pytest.mark.parametrize('web_browser', [(320, 240), (480, 360)], indirect=True)


@pytest.fixture(params=[(1710, 1121), (1470, 956), (320, 240), (480, 360)])
def browser(request):
    pass


@desktop_only
def test_github_desktop(web_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


@mobile_only
def test_github_mobile(web_browser):
    pass
