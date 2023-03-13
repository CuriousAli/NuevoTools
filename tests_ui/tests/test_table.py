import time

import pytest

from tests_ui.pages.main_page import MainPageTable


@pytest.mark.flaky
def test_price_desc_sort(browser):
    """ Checking option of desc sort of price column at main page """

    page = MainPageTable(browser)
    page.scroll_down_page_slowly()

    page.table_column_of_price.click()

    price_list = page.table_coin_prices.get_text()

    if len(price_list) == 100:
        sorted_price_list = sorted(price_list, reverse=True)
        assert sorted_price_list == price_list, F"Desc sorting of prise doesn't work {price_list}"
    else:
        assert 1 == 0, f"Rows = {len(price_list)},{price_list} "


@pytest.mark.flaky
def test_price_asc_sort(browser):
    """ Checking option of asc sort of price column at main page """

    page = MainPageTable(browser)
    page.scroll_down_page_slowly()

    page.table_column_of_price.click()
    page.table_column_of_price.click()

    price_list = page.table_coin_prices.get_text()

    if len(price_list) == 100:
        sorted_price_list = sorted(price_list, reverse=False)
        assert sorted_price_list == price_list, F"Asc sorting of prise doesn't work {price_list}"
    else:
        assert 1 == 0, f"Rows less then expected test failed{len(price_list)}"


@pytest.mark.run1
def test_get_coin_by_rank(browser, coin_rank="1", expected_name="Bitcoin"):
    page = MainPageTable(browser)
    page.scroll_down_page_slowly()

    coin_dict = dict(zip(page.table_coin_ranks.get_text(), page.table_coin_names.get_text()))

    if len(coin_dict) == 100:
        coin_name = coin_dict[coin_rank]
        assert coin_name == expected_name, f'Price is wrong. Current name of coin ranked at {coin_rank} is {coin_name}'
    else:
        assert 1 == 0, f"Rows less then expected test failed {len(coin_dict)}"

@pytest.mark.run1
def test_get_price_of_coin_by_name(browser, coin_name="Tezos"):
    page = MainPageTable(browser)
    page.scroll_down_page_slowly()

    coin_dict = dict(zip(page.table_coin_names.get_text(), page.table_coin_prices.get_text()))

    if len(coin_dict) == 100:
        coin_price = coin_dict[coin_name]
        assert coin_price == 1.06, f'Price is wrong. Current price of {coin_name} = {coin_price}'
    else:
        assert 1 == 0, f"Rows less then expected test failed{len(coin_dict)}"


@pytest.mark.flaky
def test_weekly_percentage_desc_sort(browser):
    """ Checking desc sorting of weekly growth of coins """
    page = MainPageTable(browser)
    page.scroll_down_page_slowly()

    page.table_column_of_week.click()
    coret_up = page.table_coin_week_growth_caret_up.get_text()
    coret_down = page.table_coin_week_growth_caret_down.get_text()
    weekly_list = [float(x[:-1]) for x in coret_up] + [float("-" + x[:-1]) for x in coret_down]

    if len(weekly_list) == 100:
        sorted_weekly_list = sorted(weekly_list, reverse=True)
        assert sorted_weekly_list == weekly_list, F"Desc sorting of prise doesn't work {weekly_list}"
    else:
        assert 1 == 0, f"Rows less then expected test failed{len(weekly_list)}"

@pytest.mark.run
def test_weekly_percentage_asc_sort(browser):
    """ Checking asc sorting of weekly growth of coins """
    page = MainPageTable(browser)
    page.scroll_down_page_slowly()

    page.table_column_of_week.click()
    page.table_column_of_week.click()

    coret_up = page.table_coin_week_growth_caret_up.get_text()
    coret_down = page.table_coin_week_growth_caret_down.get_text()
    weekly_list = [float("-" + x[:-1]) for x in coret_down] + [float(x[:-1]) for x in coret_up]

    if len(weekly_list) == 100:
        sorted_weekly_list = sorted(weekly_list)
        assert sorted_weekly_list == weekly_list, F"Desc sorting of prise doesn't work {weekly_list}"
    else:
        assert 1 == 0, f"Rows less then expected test failed{len(weekly_list)}"

def test_get_the_most_detrimental_coin_of_week(browser):
    pass

def test_get_the_most_profitable_coin_of_week(browser):
    pass