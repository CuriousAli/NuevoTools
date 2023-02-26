from constants import COINMARKETCAP
from tests_ui.pages.base_page import BasePage
from tests_ui.pages.elements import WebElement, ManyWebElements


class MainPageTable(BasePage):

    def __init__(self, browser, url=''):
        if not url:
            url = COINMARKETCAP

        super().__init__(browser, url)

    table_rows = ManyWebElements(xpath="//table/tbody/tr")
    table_columns = ManyWebElements(xpath="//table/thead/tr/th")

    table_column_of_price = WebElement(xpath="//table/thead/tr/th[4]/div/div")
    table_coin_prices = ManyWebElements(xpath="//table/tbody/tr/td[4]/div/a/span")
