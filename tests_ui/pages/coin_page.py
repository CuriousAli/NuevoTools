
from constants import COINMARKETCAP
from constants import COIN_PAGE

from tests_ui.pages.base_page import BasePage
from tests_ui.pages.elements import WebElement, ManyWebElements


class CoinPage(BasePage):

    def __init__(self, browser, name, url=''):
        if not url:
            url = COIN_PAGE + name
        super().__init__(browser, url)

    fullscreen_button = WebElement(xpath="//*[@id='__next']/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div/button")
    fullscreen_marker = WebElement(css_selector=".fullscreen-enabled")

