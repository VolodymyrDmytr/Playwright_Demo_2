import pytest
import allure


@pytest.mark.debug
def test_screenshot(home_page):
    allure.dynamic.title('Test to make shure that screenshots are working')
    assert 1 == 0
