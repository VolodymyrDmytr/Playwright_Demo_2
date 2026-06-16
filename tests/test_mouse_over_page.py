import pytest


@pytest.mark.mouse_over_page
def test_page_content(mouse):
    mouse.check_page_content()


@pytest.mark.mouse_over_page
@pytest.mark.parametrize(
    'link, clicks_amount',
    [
        (1, 2),
        (2, 2),
    ],
)
def test_link_clicks(mouse, link, clicks_amount):
    mouse.click_on_link_p(link, clicks_amount)
    mouse.check_amount_of_clicks_for_link(link, clicks_amount)
