import pytest


@pytest.mark.dynamic_id_page
def test_page_text(dynamic_page):
    dynamic_page.check_page_text()


@pytest.mark.dynamic_id_page
def test_button_click(dynamic_page):
    dynamic_page.click_on_btn()
