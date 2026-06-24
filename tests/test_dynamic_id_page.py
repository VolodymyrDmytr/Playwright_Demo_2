import pytest
import allure


@pytest.mark.dynamic_id_page
def test_page_text(dynamic_page):
    allure.dynamic.title('Test page content')
    dynamic_page.check_page_text()


@pytest.mark.dynamic_id_page
def test_button_click(dynamic_page):
    allure.dynamic.title('Test click on button')
    dynamic_page.click_on_btn()
