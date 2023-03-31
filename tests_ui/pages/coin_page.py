from constants import COINMARKETCAP
from tests_ui.pages.base_page import BasePage
from tests_ui.pages.elements import WebElement, ManyWebElements


class CoinPage(BasePage):
    def __init__(self, browser, url=''):
        if not url:
            url = COINMARKETCAP

        super().__init__(browser, url)

    