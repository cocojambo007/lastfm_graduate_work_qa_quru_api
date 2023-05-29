import pytest
import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selene.support.shared import browser
from helpers.help_allure import add_logs, add_screenshot, add_html, add_video
from helpers.helper import BaseSession


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='chrome'
    )


@pytest.fixture(scope="session")
def reqres():
    with BaseSession(base_url="https://reqres.in/api/") as session:
        yield session


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_name = request.config.getoption('--browser_version')
    options = Options()

    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    driver.implicitly_wait(360)
    yield
    add_logs(browser)
    add_screenshot(browser)
    add_html(browser)
    add_video(browser)
    browser.quit()
