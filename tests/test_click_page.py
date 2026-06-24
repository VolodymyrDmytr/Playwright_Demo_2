import pytest
import allure


@pytest.mark.click_page
def test_page_content(click):
    allure.dynamic.title('Test page content')
    click.check_page_content()


@pytest.mark.click_page
def test_button(click):
    allure.dynamic.title('Test buttons')
    click.click_on_button()
    click.click_on_success_btn()
