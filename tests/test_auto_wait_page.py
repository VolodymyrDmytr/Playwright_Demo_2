import pytest
from config.const import AutoWaightConst

const = AutoWaightConst()


@pytest.mark.auto_wait_page
def test_page_content(wait):
    wait.check_page_content()
    wait.check_status_text('default')


@pytest.mark.auto_wait_page
@pytest.mark.parametrize(
    'target_type',
    const.target_element_list,
)
def test_status_text(wait, target_type):
    wait.change_target_element(target_type)
    wait.check_status_text('none')

    wait.click_on_target()
    wait.check_status_text('clicked')

    wait.click_apply(3)
    wait.check_status_text('wait 3')

    wait.click_apply(5)
    wait.check_status_text('wait 5')

    wait.click_apply(10)
    wait.check_status_text('wait 10')

    wait.check_status_text('restored')


@pytest.mark.auto_wait_page
@pytest.mark.parametrize(
    'target_type',
    const.target_element_list,
)
def test_target(wait, target_type):
    wait.change_target_element(target_type)

    wait.change_target('visible')
    wait.click_apply(3)
    wait.check_is_targets_hidden()
    wait.click_on_target()

    if target_type != 'Label':
        wait.change_target('enabled')
        wait.click_apply(3)
        wait.check_is_target_disabled()
        wait.click_on_target()

    wait.change_target('on top')
    wait.click_apply(3)
    wait.check_target_is_not_clickable()
    wait.click_on_target()

    wait.change_target('non zero size')
    wait.click_apply(3)
    wait.check_targets_visibility()
    wait.click_on_target()

    if target_type == 'Label':
        wait.check_targets_text()


@pytest.mark.auto_wait_page
@pytest.mark.parametrize(
    'target_type',
    ['Input', 'Textarea'],
)
def test_target_text_fields(wait, target_type):
    data = 'Test Data'

    wait.change_target_element(target_type)
    wait.change_target('editable')
    wait.click_apply(5)
    wait.fill_target(data)
    wait.check_target_data(data)


@pytest.mark.auto_wait_page
@pytest.mark.parametrize(
    'option',
    [1, 2, 3],
)
def test_target_select(wait, option):
    wait.change_target_element('Select')
    wait.change_target('editable')
    wait.click_apply(5)
    wait.select_target_option(option)
    wait.check_target_data(const.target_options_format.format(option))
