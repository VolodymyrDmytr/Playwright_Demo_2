import pytest


@pytest.mark.disabled_input_page
def test_page_content(disabled):
    disabled.check_page_content()


@pytest.mark.disabled_input_page
def test_status_text(disabled):
    text_to_input = 'My text'

    disabled.check_status_text('Default')

    disabled.fill_field(text_to_input)
    disabled.click_on_btn()
    disabled.check_is_field_disabled()
    disabled.check_status_text('disabled')
    disabled.check_field_data(text_to_input)

    disabled.check_status_text('active')


@pytest.mark.disabled_input_page
def test_fill_field(disabled):
    text_to_input = 'My text'
    disabled.click_on_btn()
    disabled.fill_field(text_to_input)
    disabled.check_field_data(text_to_input)
