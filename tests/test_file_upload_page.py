import pytest


@pytest.mark.file_upload_page
def test_page_content(upload):
    upload.check_page_content()


@pytest.mark.file_upload_page
def test_file_upload(upload):
    upload.amount_of_uploaded_files_is_not_shown()
    upload.upload_test_file()
    upload.check_amount_of_uploaded_files(1)
    upload.check_file_name(1, upload.const.file_name)
    upload.remove_file(1)
    upload.amount_of_uploaded_files_is_not_shown()
