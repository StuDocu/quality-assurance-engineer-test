from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--host', action='store', default='http://0.0.0.0:8000/', help='Test host'
    )


@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Chrome('./driver/chromedriver')  # here we may place factory method for choosing drivers or just
    #  the usage of selenoid
    driver.get(request.config.getoption('--host'))
    driver.maximize_window()
    yield driver
    driver.close()
