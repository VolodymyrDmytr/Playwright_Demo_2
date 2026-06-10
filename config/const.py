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


class DynamicIdConst(BaseConstants):
    h3_title = 'Dynamic ID'
    text = ('Modern applications often generate dynamic IDs for elements. In '
            + 'this case ID is not a reliable attribute for using in element '
            + 'selector. By default many UI automation tools record IDs and '
            + 'this results in tests broken from the very beginning. An '
            + 'automation tool needs a way to instruct it to skip dynamic IDs '
            + 'when XPath is generated for an element.')
    h4_title1 = 'Scenario'
    bullet1 = 'Record button click.'
    bullet2 = ('Then execute your test to make sure that ID is not used for '
               + 'button identification.')
    h4_title2 = 'Playground'
    btn_text = 'Button with Dynamic ID'


class ClassAttributeConst(BaseConstants):
    h3_title = 'Class Attribute'
    text1 = ('Class attribute of an element may contain more than one class '
             + 'reference. E.g.')
    html = """<button class="btn btn-primary btn-test">"""
    text2 = ('XPath selector relying on a class must be well formed. '
             + 'For example, the following will not work:')
    bash1 = "//button[@class='btn-primary']"
    text3 = 'Correct variant is'
    bash2 = ("//button[contains(concat(' ', normalize-space(@class), ' '), ' "
             + " btn-primary ')]")
    h4_title1 = 'Scenario'
    bullet1 = 'Record primary (blue) button click and press ok in alert popup.'
    bullet2 = ('Then execute your test to make sure that it can identify the '
               + 'button using btn-primary class.')
    h4_title2 = 'Playground'
    btn_text = 'Button'
    alert_text = 'Primary button pressed'


class HiddenLayersConst(BaseConstants):
    h3 = 'Hidden Layers'
    text = ('Some applications use DOM caching techniques. For example, if a '
            + 'user follows a multi step process and each step requires '
            + 'filling data into a form then forms may be cached at the client'
            + ' side along the way. It allows to quickly navigate back and '
            + 'forward through the steps without requesting data from a '
            + 'server. When form is cached it just pushed on-top of z-order '
            + 'stack. It means that an element may be still present in the DOM'
            + ' tree but overlapped with another layer of elements. In this '
            + 'case it is important that a test does not interact with '
            + 'inactive elements becasue they are invisible to a user.')
    h4_title1 = 'Scenario'
    bullet1 = ('Record button click and then duplicate the button click step '
               + 'in your test.')
    bullet2 = ('Execute the test to make sure that green button can not be hit'
               + ' twice.')
    h4_title2 = 'Playground'
    btn_text = 'Button'


class LoadDelaysConst(BaseConstants):
    h3 = 'Load Delays'
    text = ('Server response may often come with an unpredictable delay. So a'
            + ' test must be able to patiently wait for page loaded event from'
            + ' a browser.')
    h4_title1 = 'Scenario'
    bullet1 = ('Navigate to Home page and record Load Delays link click and'
               + ' button click on this page.')
    bullet2 = 'Then play the test. It should wait until page is loaded.'
    h4_title2 = 'Playground'
    btn_text = 'Button Appearing After Delay'
