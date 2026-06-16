import pytest


@pytest.mark.overlapped_element_page
def test_page_content(overlapped):
    overlapped.check_page_content()


@pytest.mark.overlapped_element_page
@pytest.mark.parametrize(
    'ids, name, subj',
    [
        ('24', 'Test', 'QA'),
    ],
)
def test_fields(overlapped, ids, name, subj):
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
