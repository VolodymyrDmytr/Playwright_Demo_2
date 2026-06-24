import pytest
import allure


@pytest.mark.verify_text_page
def test_page_content(verify):
    allure.dynamic.title('Test page content')
    verify.check_page_content()


@pytest.mark.verify_text_page
def test_text_finding(verify):
    allure.dynamic.title('Test text finding')
    verify.find_text()
