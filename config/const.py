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
    timeout = 25000

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


class PageConst:
    h4_title1 = 'Scenario'
    h4_title2 = 'Playground'


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


class DynamicIdConst(BaseConstants, PageConst):
    h3_title = 'Dynamic ID'
    text = ('Modern applications often generate dynamic IDs for elements. In '
            + 'this case ID is not a reliable attribute for using in element '
            + 'selector. By default many UI automation tools record IDs and '
            + 'this results in tests broken from the very beginning. An '
            + 'automation tool needs a way to instruct it to skip dynamic IDs '
            + 'when XPath is generated for an element.')
    bullet1 = 'Record button click.'
    bullet2 = ('Then execute your test to make sure that ID is not used for '
               + 'button identification.')
    btn_text = 'Button with Dynamic ID'


class ClassAttributeConst(BaseConstants, PageConst):
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
    bullet1 = 'Record primary (blue) button click and press ok in alert popup.'
    bullet2 = ('Then execute your test to make sure that it can identify the '
               + 'button using btn-primary class.')
    btn_text = 'Button'
    alert_text = 'Primary button pressed'


class HiddenLayersConst(BaseConstants, PageConst):
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
    bullet1 = ('Record button click and then duplicate the button click step '
               + 'in your test.')
    bullet2 = ('Execute the test to make sure that green button can not be hit'
               + ' twice.')
    btn_text = 'Button'


class LoadDelaysConst(BaseConstants, PageConst):
    h3 = 'Load Delays'
    text = ('Server response may often come with an unpredictable delay. So a'
            + ' test must be able to patiently wait for page loaded event from'
            + ' a browser.')
    bullet1 = ('Navigate to Home page and record Load Delays link click and'
               + ' button click on this page.')
    bullet2 = 'Then play the test. It should wait until page is loaded.'
    btn_text = 'Button Appearing After Delay'


class AjaxDataConst(BaseConstants, PageConst):
    h3 = 'AJAX Data'
    text = ('An element may appear on a page after processing of an AJAX '
            + 'request to a web server. A test should be able to wait for an'
            + ' element to show up.')
    bullet1 = ('Record the following steps. Press the button below and wait '
               + 'for data to appear (15 seconds), click on text of the loaded'
               + ' label.')
    bullet2 = ('Then execute your test to make sure it waits for label text to'
               + ' appear.')
    btn_text = 'Button Triggering AJAX Request'
    success_text = 'Data loaded with AJAX get request.'


class ClientSideDelayConst(BaseConstants, PageConst):
    h3 = 'Client Side Delay'
    text = ('An element may appaear on a page after heavy JavaScript '
            + 'processing on a client side. A test should be able to wait for '
            + 'an element to show up.')
    bullet1 = ('Record the following steps. Press the button below and wait '
               + 'for data to appear (15 seconds), click on text of the loaded'
               + ' label.')
    bullet2 = ('Then execute your test to make sure it waits for label text '
               + 'to appear.')
    btn_text = 'Button Triggering Client Side Logic'
    success_text = 'Data calculated on the client side.'


class ClickConst(BaseConstants, PageConst):
    h3 = 'Click'
    text = ('Physical mouse click and DOM event emulated click are differently'
            + ' handled by browsers. There are still cases, with sometimes'
            + ' hardly identifiable reasons, when an event based click does '
            + 'not work. The solution for this problem is emulating physical '
            + 'mouse click. This page is specifically designed to ignore event'
            + ' based click.')
    bullet1 = 'Record button click. The button becomes green after clicking.'
    bullet2 = ('Then execute your test to make sure that it is able to click '
               + 'the button.')
    btn_text = 'Button That Ignores DOM Click Event'


class TextInputConst(BaseConstants, PageConst):
    h3 = 'Text Input'
    text = ('Entering text with physical keyboard can be different from '
            + 'sending DOM events to an element. This page is specifically '
            + 'desined to illustrate this problem. There are cases when '
            + 'attempts to set a text via DOM events lead to nowhere and the '
            + 'only way to proceed is to emulate real keyboard input at '
            + 'OS level.')
    bullet1 = ('Record setting text into the input field and pressing the '
               + 'button.')
    bullet2 = ('Then execute your test to make sure that the button name '
               + 'is changing.')
    field_title = 'Set New Button Name'
    field_placeholder = 'MyButton'
    btn_text = "Button That Should Change it's Name Based on Input Value"


class ScrollbarsConst(BaseConstants, PageConst):
    h3 = 'Scrollbars'
    text = ('An application may use native or custom scrollbars and some '
            + 'elements may be out of view. A test scenario may require to '
            + 'ensure that an element is visible on screen and this may '
            + 'require scrolling.')
    bullet1 = 'Find a button in the scroll view and record button click.'
    bullet2 = ('Update your test to automatically scroll the button into a '
               + 'visible area.')
    bullet3 = 'Then execute your test to make sure it works.'
    btn_text = 'Hiding Button'


class DynamicTableConst(BaseConstants, PageConst):
    h3 = 'Dynamic Table'
    text = ('Below you see a table where columns and rows change their '
            + 'position upon page reload. Values in cells are random. The '
            + 'table is based on DIVs with ARIA attributes. See WAI-ARIA table'
            + ' design pattern for details.')
    bullet1 = 'For Chrome process get value of CPU load.'
    bullet2 = 'Compare it with value in the yellow label.'
    expected_text = 'Chrome CPU: {}'
    browser = 'Chrome'
    column = 'CPU'
