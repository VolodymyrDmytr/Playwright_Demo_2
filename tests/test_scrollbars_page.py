import pytest
import allure


@pytest.mark.scrollbars_page
def test_page_content(scroll):
    allure.dynamic.title('Test page content')
    scroll.check_page_content()


@pytest.mark.scrollbars_page
def test_button(scroll):
    allure.dynamic.title('Test click on button')
    scroll.click_on_button()
