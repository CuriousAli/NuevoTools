import pytest

from tests_ui.pages.coin_page import CoinPage


def test_open_weekly_chart_data(browser):
    pass

def test_open_monthly_chart_data(browser):
    pass

def test_open_last_three_month_chart_data(browser):
    pass

@pytest.mark.run
def test_open_fullscreen_chart_data_mode(browser, name='bitcoin'):
    page = CoinPage(browser, name=name)
    page.fullscreen_button.click()
    assert page.fullscreen_marker.is_presented(), f"Fullscreen of chart data didn't open"

def test_open_markets_subsection(browser):
    pass

def test_market_price_q_desc_sort(browser):
    pass

def test_market_price_q_asc_sort(browser):
    pass

def test_market_volumes_desc_sort(browser):
    pass

def test_market_volumes_asc_sort(browser):
    pass

def test_get_market_name_with_the_highest_price(browser):
    pass

def test_get_market_name_with_the_highest_price(browser):
    pass