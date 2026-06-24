import pytest
import allure


@pytest.mark.client_side_delay_page
def test_page_content(delay):
    allure.dynamic.title('Test page content')
    delay.check_page_content()


@pytest.mark.client_side_delay_page
def test_button(delay):
    allure.dynamic.title('Test buttons')
    delay.click_on_button()
    delay.check_success_text()
    delay.click_on_text()
