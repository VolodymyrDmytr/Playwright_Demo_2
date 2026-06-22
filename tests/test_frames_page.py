import pytest

from config.const import FramesConst

const = FramesConst()


@pytest.mark.frames_page
def test_page_content(iframe):
    iframe.check_page_content()
    iframe.check_status_text_is_not_shown(1)
    iframe.check_status_text_is_not_shown(2)


@pytest.mark.frames_page
@pytest.mark.parametrize(
    'iframe_numb',
    [1, 2],
)
def test_edit_btn(iframe, iframe_numb):
    iframe.click_on_edit_btn(iframe_numb)
    iframe.check_status_text(iframe_numb, const.btn1)


@pytest.mark.frames_page
@pytest.mark.parametrize(
    'iframe_numb',
    [1, 2],
)
def test_submit_btn(iframe, iframe_numb):
    iframe.click_on_submit_btn(iframe_numb)
    iframe.check_status_text(iframe_numb, const.btn2)


@pytest.mark.frames_page
@pytest.mark.parametrize(
    'iframe_numb',
    [1, 2],
)
def test_click_btn(iframe, iframe_numb):
    iframe.click_on_click_btn(iframe_numb)
    iframe.check_status_text(iframe_numb, const.btn3)


@pytest.mark.frames_page
@pytest.mark.parametrize(
    'iframe_numb',
    [1, 2],
)
def test_primary_btn(iframe, iframe_numb):
    iframe.click_on_primary_btn(iframe_numb)
    iframe.check_status_text(iframe_numb, const.btn4)
