import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

@pytest.fixture(scope="function")
def browser():
    #profile = FirefoxProfile()
    #profile.set_preference("permissions.default.image",2)
    options = Options()
    #options.profile=profile
    options.binary_location = 'C:\\FirefoxPortable\\App\\Firefox64\\Firefox.exe'
    options.page_load_strategy = 'normal'
    #options.timeouts= {'implicit':600000,'pageLoad':600000,'script':600000}
    executable_path = 'C:\\FirefoxPortable\\geckodriver.exe'
    driver = webdriver.Firefox(service=Service(executable_path=executable_path), options=options)
    yield driver
    driver.quit()