import pytest
import allure


@pytest.mark.class_attribute_page
def test_page_content(class_attr):
    allure.dynamic.title('Test page content')
    class_attr.check_page_title('Class Attribute')
    class_attr.check_page_text()


@pytest.mark.class_attribute_page
@pytest.mark.parametrize('btn', ['Orange', 'Green'])
def test_no_action_buttons(class_attr, btn):
    allure.dynamic.title(f'Test {btn} button without actions')
    class_attr.click_btn(btn)
    class_attr.click_btn(btn)


@pytest.mark.class_attribute_page
def test_button_with_action(class_attr):
    allure.dynamic.title('Test button with alert')

    class_attr.accept_and_check_alert_text()
    class_attr.accept_alert()
