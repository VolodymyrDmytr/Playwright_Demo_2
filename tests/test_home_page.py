import pytest


@pytest.mark.home_page
def test_url(home_page):
    home_page.check_url(home_page.const.base_url)


@pytest.mark.home_page
def test_page_title(home_page):
    home_page.check_page_title(home_page.const.title_on_page)


@pytest.mark.home_page
def test_page_data(home_page):
    home_page.check_text()
    home_page.check_image()
    home_page.check_image_text()


@pytest.mark.home_page
@pytest.mark.parametrize('card_nmb', [i for i in range(0, 28)])
def test_cards_data(home_page, card_nmb):
    card_data = home_page.const.card_data(card_nmb)
    home_page.check_block_data(
        card_data.card_title,
        card_data.card_description,
        card_data.card_ids,
    )


@pytest.mark.home_page
@pytest.mark.parametrize('card_nmb', [i for i in range(0, 28)])
def test_cards_urls(home_page, card_nmb):
    card_data = home_page.const.card_data(card_nmb)
    page_url = home_page.const.url_by_title(card_data.card_title)

    home_page.click_on_link(card_data.card_title)
    home_page.check_page_title(card_data.page_title)
    home_page.check_url(page_url)
