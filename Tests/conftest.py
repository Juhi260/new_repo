from pytest import fixture
from selenium import webdriver
from Library.readProperties import ReadConfig
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

#When a test function requires the setup fixture,
# pytest will automatically call the setup() function.
#It will execute everything up to the yield statement,
# which includes opening the browser and navigating to the URL.
@fixture
def setup():
    Url=ReadConfig.getUrl()
    driver = webdriver.Chrome()
    driver.get(Url)  # 10 seconds wait
    driver.maximize_window()
    yield driver
    driver.close()

@fixture
def pages(driver):
    from POM.HomePage import HomePage
    from POM.MobilePage import MobilePage
    # Initialize page objects with the driver
    homepage = HomePage(driver)
    mobilepage = MobilePage(driver)
    # Return them as attributes of a Page object (you could also return a dictionary if preferred)
    class Page:
        def __init__(self):
            self.homepage = homepage
            self.mobilepage = mobilepage
    return Page()#This line returns an instance of the Page class,
    # which contains the homepage and mobilepage objects as attributes.
    # When the pages fixture is used in a test,
    # it will provide access to both the HomePage and MobilePage objects through
    # the returned Page instance.