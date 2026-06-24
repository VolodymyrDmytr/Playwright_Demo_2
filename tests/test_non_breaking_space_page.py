import pytest
import allure


@pytest.mark.nbsp_page
def test_page_content(nbsp):
    allure.dynamic.title('Test page content')
    nbsp.check_page_content()


@pytest.mark.nbsp_page
def test_button_click(nbsp):
    allure.dynamic.title('Test click on button')
    nbsp.click_on_btn()
