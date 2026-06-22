import pytest


@pytest.mark.scroll_to_click_page
def test_page_content(scroll_click):
    scroll_click.check_page_content()
    scroll_click.check_status_text(0)


@pytest.mark.scroll_to_click_page
def test_btn1(scroll_click):
    scroll_click.click_on_btn1()
    scroll_click.check_status_text(1)


@pytest.mark.scroll_to_click_page
def test_btn2(scroll_click):
    scroll_click.click_on_btn2()
    scroll_click.check_status_text(1)


@pytest.mark.scroll_to_click_page
def test_btn3(scroll_click):
    scroll_click.click_on_btn3()
    scroll_click.check_status_text(1)


@pytest.mark.scroll_to_click_page
def test_btn4(scroll_click):
    scroll_click.click_on_btn4()
    scroll_click.check_status_text(1)


@pytest.mark.scroll_to_click_page
def test_status_text(scroll_click):
    scroll_click.check_status_text(0)

    scroll_click.click_on_btn1()
    scroll_click.check_status_text(1)

    scroll_click.click_on_btn2()
    scroll_click.check_status_text(2)

    scroll_click.click_on_btn3()
    scroll_click.check_status_text(3)

    scroll_click.click_on_btn4()
    scroll_click.check_status_text(4)
