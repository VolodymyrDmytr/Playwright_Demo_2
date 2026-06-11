import pytest


@pytest.mark.text_input_page
def test_page_content(text):
    text.check_page_content()


@pytest.mark.text_input_page
@pytest.mark.parametrize('data', ['Button', 'Button 123 !', '123', '%$'])
def test_button(text, data):
    text.change_button_name(data)
