import pytest
import allure


@pytest.mark.clear_input_page
def test_page_content(clear_input):
    allure.dynamic.title('Test page content')
    clear_input.check_page_content()
    clear_input.check_status_text(clear_input.fields_amount())


@pytest.mark.clear_input_page
@pytest.mark.parametrize(
    'field',
    [i for i in range(1, 10)],
)
def test_fields(clear_input, field):
    allure.dynamic.title(f'Test field {field}')

    if field != 5:
        data = 'Some text'
    else:
        data = '52'

    clear_input.remove_data(field)
    clear_input.check_status_text(clear_input.fields_amount() - 1)
    clear_input.fill_data(field, data)
    clear_input.check_status_text(clear_input.fields_amount())


@pytest.mark.clear_input_page
def test_removing_data(clear_input):
    allure.dynamic.title('Test removing data from fields')
    fields_amount = clear_input.fields_amount()

    for i in range(1, fields_amount + 1):
        clear_input.remove_data(i)
        clear_input.check_status_text(fields_amount - i)
