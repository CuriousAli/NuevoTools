import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="function")
def browser():
    option = Options()
    #option.headless = True
    browser = webdriver.Chrome(options=option)
    browser.set_window_size(1700, 1100)
    yield browser
    browser.quit()

