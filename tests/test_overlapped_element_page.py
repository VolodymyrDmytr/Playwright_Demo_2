import pytest
import allure


@pytest.mark.overlapped_element_page
def test_page_content(overlapped):
    allure.dynamic.title('Test page content')
    overlapped.check_page_content()


@pytest.mark.overlapped_element_page
@pytest.mark.parametrize(
    'ids, name, subj',
    [
        ('24', 'Test', 'QA'),
    ],
)
def test_fields(overlapped, ids, name, subj):
    allure.dynamic.title(
        f'Test fields id = {ids}, name = {name} and subject = {subj}')
    overlapped.fill_fields(
        ids,
        name,
        subj,
    )
    overlapped.check_fields_data(
        ids,
        name,
        subj,
    )
