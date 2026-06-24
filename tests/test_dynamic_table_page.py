import pytest
import allure


@pytest.mark.dynamic_table_page
def test_page_content(table):
    allure.dynamic.title('Test page content')
    table.check_page_content()


@pytest.mark.dynamic_table_page
def test_table_data(table):
    allure.dynamic.title('Test table data')
    table.check_is_data_as_expected()
