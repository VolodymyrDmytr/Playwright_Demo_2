import pytest


@pytest.mark.load_delays_page
def test_page_content(load):
    load.check_page_content()


@pytest.mark.load_delays_page
def test_button(load):
    load.click_on_button()
