import pytest


@pytest.mark.scrollbars_page
def test_page_content(scroll):
    scroll.check_page_content()


@pytest.mark.scrollbars_page
def test_button(scroll):
    scroll.click_on_button()
