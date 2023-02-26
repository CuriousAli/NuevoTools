import pytest

from tests_ui.pages.main_page import MainPageTable


def test_price_desc_sort(browser):
    """ Checking option of desc sort of price column at main page """

    page = MainPageTable(browser)
    rows = page.table_rows.count()

    page.table_column_of_price.click()
    if rows == 100:
        price_list = page.table_coin_prices.get_text()
        sorted_price_list = sorted(price_list, reverse=True)
        assert sorted_price_list == price_list, F"Desc sorting of prise doesn't work {price_list}"


def test_price_asc_sort(browser):
    """ Checking option of asc sort of price column at main page """

    page = MainPageTable(browser)
    rows = page.table_rows.count()

    page.table_column_of_price.click()
    page.table_column_of_price.click()
    if rows == 100:
        price_list = page.table_coin_prices.get_text()
        sorted_price_list = sorted(price_list, reverse=False)
        assert sorted_price_list == price_list, F"Desc sorting of prise doesn't work {price_list}"

def test_get_coin_by_price(browser):
    pass

def test_get_price_of_coin_by_name(browser):
    pass

def test_weekly_percentage_desc_sort(browser):
    pass

def test_weekly_percentage_asc_sort(browser):
    pass

def test_get_the_most_detrimental_coin_of_week(browser):
    pass

def test_get_the_most_profitable_coin_of_week(browser):
    pass