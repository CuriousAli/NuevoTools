from constants import COINMARKETCAP
from tests_ui.pages.base_page import BasePage
from tests_ui.pages.elements import WebElement, ManyWebElements


class MainPageTable(BasePage):

    def __init__(self, browser, url=''):
        if not url:
            url = COINMARKETCAP

        super().__init__(browser, url)

    footer = WebElement(css_selector="//div[contains(text(), 'CoinMarketCap. All rights reserved')]")

    table_rows = ManyWebElements(xpath="//table/tbody/tr")
    table_columns = ManyWebElements(xpath="//table/thead/tr/th")

    table_column_rank = WebElement(xpath="//table/thead/tr/th[2]/div/div")
    table_coin_ranks = ManyWebElements(xpath="//table/tbody/tr/td[2]/p")

    table_column_of_name = WebElement(xpath="//table/thead/tr/th[3]/div/div")
    table_coin_names = ManyWebElements(xpath="//table/tbody/tr/td[3]/div/a/div/div/p")

    table_column_of_price = WebElement(xpath="//table/thead/tr/th[4]/div/div")
    table_coin_prices = ManyWebElements(xpath="//table/tbody/tr/td[4]/div/a/span")

    table_column_of_week = WebElement(xpath="//table/thead/tr/th[7]/div/div/div")
    table_coin_week_growth_caret_up = ManyWebElements(xpath="//table/tbody/tr/td[7]/span/span[@class='icon-Caret-up']/..")
    table_coin_week_growth_caret_down = ManyWebElements(xpath="//table/tbody/tr/td[7]/span/span[@class='icon-Caret-down']/..")
