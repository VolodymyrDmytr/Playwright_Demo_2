from pathlib import Path
import json


class CardData:

    def __init__(
            self,
            card_ids: int = 0,
            card_title: str = '',
            page_title: str = '',
            card_description: str = '',
            card_url: str = '',
    ):
        self.card_ids = card_ids
        self.card_title = card_title
        self.page_title = page_title
        self.card_description = card_description
        self.card_url = card_url

    # Path to json
    data_file = Path(__file__).parent / 'cards.json'

    def cards(self) -> list:
        with open(self.data_file) as f:
            data = json.load(f)['cards_data']
        return data

    @property
    def cards_amount(self) -> int:
        return len(self.cards())

    def card_data(
            self,
            number: int,
    ) -> object:
        if number > self.cards_amount:
            return {'Error': 'Missing such number in cards.json file'}

        data = self.cards()
        for i in range(0, self.cards_amount):
            if number == data[i]['id']:
                card = data[i]
                break

        return CardData(
            card_ids=card['id'],
            card_title=card['card_title'],
            page_title=card['page_title'],
            card_description=card['description'],
            card_url=card['url'],
        )


class BaseConstants(CardData):
    base_url = 'http://uitestingplayground.com/'

    def url_by_title(
            self,
            data: str,
    ) -> str:
        """Page url by title

        Args:
            data (str): page title

        Returns:
            str: page url
        """
        cards = self.cards()
        for i in range(0, self.cards_amount):
            if cards[i]['card_title'] == data:
                return f"{self.base_url}{cards[i]['url']}"


class HomePageConst(BaseConstants):
    # Data
    title_on_page = 'UI Test Automation Playground'
    h1_text = 'UI Test AutomationPlayground'
    quote = 'Quality is not an act, it is a habit.'
    author = 'Aristotle'
    purpose_text = ('The purpose of this website is to provide a platform for '
                    + 'sharpening UI test automation skills. Use it to '
                    + 'practice with your test automation tool. Use it to '
                    + 'learn test automation techniques.')
    text = ('Different automation pitfalls appearing in modern web '
            + 'applications are described and emulated below.')
    img_alt = 'Responsive image'
    img_text = "Rubik's Cube is licensed under CC 4.0 BY-NC"
