import pytest


@pytest.mark.alerts_page
def test_page_content(alerts):
    alerts.check_page_content()


@pytest.mark.alerts_page
def test_alert(alerts):
    alerts.click_alert_btn()
    alerts.check_dialog_text(alerts.const.alert_text)
    alerts.accept_dialog()


@pytest.mark.alerts_page
def test_confirm_ok(alerts):
    alerts.click_confirm_btn()
    alerts.check_dialog_text(alerts.const.confirm_text)
    alerts.accept_dialog()
    alerts.check_dialog_text(alerts.const.confirm_text_ok)


@pytest.mark.alerts_page
def test_confirm_cancel(alerts):
    alerts.click_confirm_btn()
    alerts.check_dialog_text(alerts.const.confirm_text)
    alerts.cancel_dialog()
    alerts.check_dialog_text(alerts.const.confirm_text_cancel)


@pytest.mark.alerts_page
@pytest.mark.parametrize(
    'data',
    [
        'cats', 'dogs', 'data',
    ],
)
def test_prompt_ok(alerts, data):
    alerts.click_prompt_btn()
    alerts.check_dialog_text(alerts.const.prompt_text)
    alerts.accept_prompt(data)
    alerts.check_dialog_text(
        alerts.const.prompt_text_submit_format.format(data))
    alerts.accept_dialog()


@pytest.mark.alerts_page
@pytest.mark.parametrize(
    'data',
    [
        '', 'dogs', 'cats', 'data',
    ],
)
def test_prompt_cancel(alerts, data):
    alerts.click_prompt_btn()
    alerts.check_dialog_text(alerts.const.prompt_text)
    alerts.cancel_prompt(data)
    alerts.check_dialog_text(alerts.const.prompt_text_cancel)
    alerts.accept_dialog()
