import pytest


@pytest.mark.nbsp_page
def test_page_content(nbsp):
    nbsp.check_page_content()


@pytest.mark.nbsp_page
def test_button_click(nbsp):
    nbsp.click_on_btn()
