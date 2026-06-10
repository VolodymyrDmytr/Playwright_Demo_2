import pytest


@pytest.mark.hidden_layers_page
def test_page_content(hidden):
    hidden.check_page_content()


@pytest.mark.hidden_layers_page
def test_button(hidden):
    hidden.click_on_button()
    hidden.check_is_success()
