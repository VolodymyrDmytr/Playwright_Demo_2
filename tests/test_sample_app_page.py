import pytest

from config.const import SampleAppConst

const = SampleAppConst()


@pytest.mark.sample_app_page
def test_page_content(app):
    app.check_page_content()
    app.check_info_text_default_error('Default')


@pytest.mark.sample_app_page
@pytest.mark.parametrize(
    'name, password',
    [
        ('', ''),
        ('', const.password),
        ('Name', f'{const.password}1'),
    ],
)
def test_invalid_data(app, name, password):
    app.fill_form(name, password)
    app.click_on_btn()
    app.check_info_text_default_error('Error')


@pytest.mark.sample_app_page
@pytest.mark.parametrize(
    'name',
    [
        '123', 'Name', 'name', '!@#$',
    ],
)
def test_valid_data(app, name):
    app.fill_form(name, const.password)
    app.click_on_btn()
    app.check_success_info_text(name)
