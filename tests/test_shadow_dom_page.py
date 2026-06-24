import pytest
import allure


@pytest.mark.shadow_dom_page
def test_page_content(shadow_dom):
    allure.dynamic.title('Test page content')
    shadow_dom.check_page_content()


@pytest.mark.shadow_dom_page
def test_guid_generator_field(shadow_dom):
    allure.dynamic.title('Test GUID field')
    shadow_dom.check_guid_field('')
    shadow_dom.click_generate_guid()
    # data = shadow_dom.copy_guid_btn() - Error in console after click on page
    data = shadow_dom.get_generated_guid()
    shadow_dom.check_guid_field(data)
    shadow_dom.check_field_is_not_empty()
