import pytest
import allure


@pytest.mark.ajax_data_page
def test_page_content(ajax):
    allure.dynamic.title('Test page content')
    ajax.check_page_content()


@pytest.mark.ajax_data_page
def test_button(ajax):
    allure.dynamic.title('Test button click')
    ajax.click_on_button()
    ajax.check_success_text()


@pytest.mark.ajax_data_page
def test_response(ajax):
    allure.dynamic.title('Test ajax response')
    ajax.check_response()
