import pytest
import allure


@pytest.mark.load_delays_page
def test_page_content(load):
    allure.dynamic.title('Test page content')
    load.check_page_content()


@pytest.mark.load_delays_page
def test_button(load):
    allure.dynamic.title('Test click on button')
    load.click_on_button()
