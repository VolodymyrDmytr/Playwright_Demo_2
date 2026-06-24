import pytest
import allure


@pytest.mark.visibility_page
def test_page_content(visibility):
    allure.dynamic.title('Test page content')
    visibility.check_page_content()


@pytest.mark.visibility_page
def test_hide_btn(visibility):
    allure.dynamic.title('Test hide button')
    # assert visibility.check_are_buttons_in_correct_visibility() is False
    visibility.click_hide_btn()
    visibility.check_are_buttons_in_correct_visibility()
