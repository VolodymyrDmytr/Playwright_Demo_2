import pytest


@pytest.mark.ajax_data_page
def test_page_content(ajax):
    ajax.check_page_content()


@pytest.mark.ajax_data_page
def test_button(ajax):
    ajax.click_on_button()
    ajax.check_success_text()


@pytest.mark.ajax_data_page
def test_response(ajax):
    ajax.check_response()
