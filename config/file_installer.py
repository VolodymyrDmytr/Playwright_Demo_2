import os
from urllib import request

from config.const import FileUploadConst

const = FileUploadConst()

name = const.file_name
file_path = const.path_to_test_file
url = f'https://pdfobject.com/pdf/{name}'


def install_file_if_it_is_not_exist() -> None:
    if not os.path.exists(file_path):
        request.urlretrieve(
            url,
            file_path,
        )
