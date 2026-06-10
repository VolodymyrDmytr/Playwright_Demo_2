import pytest


@pytest.mark.client_side_delay_page
def test_page_content(delay):
    delay.check_page_content()


@pytest.mark.client_side_delay_page
def test_button(delay):
    delay.click_on_button()
    delay.check_success_text()
    delay.click_on_text()
