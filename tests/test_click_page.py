import pytest


@pytest.mark.click_page
def test_page_content(click):
    click.check_page_content()


@pytest.mark.click_page
def test_button(click):
    click.click_on_button()
    click.click_on_success_btn()
