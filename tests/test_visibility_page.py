import pytest


@pytest.mark.visibility_page
def test_page_content(visibility):
    visibility.check_page_content()


@pytest.mark.visibility_page
def test_hide_btn(visibility):
    # assert visibility.check_are_buttons_in_correct_visibility() is False
    visibility.click_hide_btn()
    visibility.check_are_buttons_in_correct_visibility()
