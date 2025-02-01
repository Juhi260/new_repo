from pytest import fixture
from selenium import webdriver
from POM.HomePage import HomePage
from POM.MobilePage import MobilePage
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@fixture
def driver():
    driver_ = webdriver.Chrome()
    driver_.get("https://www.flipkart.com/")
    driver_.maximize_window()
    yield driver_
    driver_.close()

@fixture
def pages(driver):
    # Initialize page objects with the driver
    homepage = HomePage(driver)
    mobilepage = MobilePage(driver)

    # Return them as attributes of a Page object (you could also return a dictionary if preferred)
    class Page:
        def __init__(self):
            self.homepage = homepage
            self.mobilepage = mobilepage

    return Page()