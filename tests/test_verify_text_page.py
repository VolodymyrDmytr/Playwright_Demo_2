import pytest


@pytest.mark.verify_text_page
def test_page_content(verify):
    verify.check_page_content()


@pytest.mark.verify_text_page
def test_text_finding(verify):
    verify.find_text()
