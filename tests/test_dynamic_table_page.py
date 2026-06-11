import pytest


@pytest.mark.dynamic_table_page
def test_page_content(table):
    table.check_page_content()


@pytest.mark.dynamic_table_page
def test_table_data(table):
    table.check_is_data_as_expected()
