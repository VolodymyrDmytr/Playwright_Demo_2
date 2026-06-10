import pytest


@pytest.mark.class_attribute_page
def test_page_content(class_attr):
    class_attr.check_page_title('Class Attribute')
    class_attr.check_page_text()


@pytest.mark.class_attribute_page
@pytest.mark.parametrize('btn', ['Orange', 'Green'])
def test_no_action_buttons(class_attr, btn):
    class_attr.click_btn(btn)
    class_attr.click_btn(btn)


@pytest.mark.class_attribute_page
def test_button_with_action(class_attr):
    class_attr.accept_and_check_alert_text()
    class_attr.accept_alert()
