import pytest
import allure


@pytest.mark.hidden_layers_page
def test_page_content(hidden):
    allure.dynamic.title('Test page content')
    hidden.check_page_content()


@pytest.mark.hidden_layers_page
def test_button(hidden):
    allure.dynamic.title('Test click on button')
    hidden.click_on_button()
    hidden.check_is_success()
