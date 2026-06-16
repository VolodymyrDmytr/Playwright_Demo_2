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


class VerifyTextConst(BaseConstants, PageConst):
    h3 = 'Verify Text'
    text1 = ('In general inner text of a DOM element is different from '
             + 'displayed on screen. Browsers normalize text upon rendering, '
             + 'but DOM nodes contain text as it is in HTML markup. For '
             + 'example a browser may show the text as')
    text2 = 'and the text of the DOM element can be'
    text3 = ('Take this fact into account when searching for an element using'
             + " it's text value. ")
    bullet1 = 'Create a test that finds an element with Welcome... text.'
    table_title1 = 'Does not work'
    xpath1 = "//span[.='Welcome UserName!']"
    table_title2 = 'Works'
    xpath2 = "//span[normalize-space(.)='Welcome UserName!']"
    text_to_find = 'Welcome UserName!'
    fake_text = 'Hello UserName!'


class ProgressBarConst(BaseConstants, PageConst):
    h3 = 'Progress Bar'
    text = ('A web application may use a progress bar to reflect state of some'
            + ' lengthy process. Thus a test may need to read the value of a '
            + 'progress bar to determine if it is time to proceed or not.')
    bullet = ('Create a test that clicks Start button and then waits for the '
              + 'progress bar to reach 75%. Then the test should click Stop. '
              + 'The less the differnce between value of the stopped progress'
              + ' bar and 75% the better your result.')
    btn_start = 'Start'
    btn_stop = 'Stop'
    result = 'Result: {}, duration:'
    default_result = 'Result: n/a'


class VisibilityConst(BaseConstants, PageConst):
    h3 = 'Visibility'
    txt = 'Checking if element is visible on screen may be a non trivial task.'
    bullets1_1 = 'An element may be removed (simplest case),'
    bullets1_2 = 'it may have zero height or width,'
    bullets1_3 = 'it may be covered by another element,'
    bullets1_4 = ('it may be hidden using styles: opacity: 0, visibility: '
                  + 'hidden, display: none,')
    bullets1_5 = 'or moved offscreen.'
    bullets2_1 = 'Learn locators of all buttons.'
    bullets2_2 = 'In your testing scenario press Hide button.'
    bullets2_3 = 'Determine if other buttons visible or not.'
    btn_blue = 'Hide'
    btn_red = 'Removed'
    btn_yellow = 'Zero Width'
    btn_green = 'Overlapped'
    btn_info_1 = 'Opacity 0'
    btn_info_2 = 'Visibility Hidden'
    btn_info_3 = 'Display None'
    btn_info_4 = 'Offscreen'


class SampleAppConst(BaseConstants, PageConst):
    h3 = 'Sample App'
    text = ('Fill in and submit the form. For successfull login use any '
            + 'non-empty user name and `pwd` as password.')
    info_text_default = 'User logged out.'
    info_text_success = 'Welcome, {}!'
    info_text_error = 'Invalid username/password'
    btn_text = 'Log In'
    password = 'pwd'


class MouseOverConst(BaseConstants, PageConst):
    h3 = 'Mouse Over'
    text1 = (
        'Placing mouse over an element may lead to changes in the DOM '
        + 'tree. For example the element may be modified or replaced. It '
        + 'means if you keep a reference to the original element and will'
        + ' try to click on it - it may not work (stale element problem).'
        )
    text2 = 'This puzzle complicates both recording and playback of a test.'
    bullet1 = 'Record 2 consecutive link clicks.'
    bullet2 = ('Execute the test and make sure that click count is increasing '
               + 'by 2.')
    text3 = ('The link below will be replaced and new title assigned to it '
             + 'when you place mouse over it. Click on it to increase the '
             + 'click count.')
    link1 = 'Click me'
    text4_counter = 'The link above clicked {} times.'
    text5 = ('The link below will be replaced with identical one when you '
             + 'place mouse over it. Click on it to increase the click count.')
    link2 = 'Link Button'
    text6_counter = 'The link above clicked {} times.'


class NonBreakingSpaceConst(BaseConstants, PageConst):
    h3 = 'Non-Breaking Space'
    text = ('There are cases in test automation when something should '
            + 'obviously work but for some reason it does not. Searching for '
            + 'an element by its text is one of those cases. Text caption may '
            + 'contain non-breaking spaces that have no visual difference from'
            + ' generic spaces.')
    locator = "//button[text()='My Button']"
    bullet1 = ('Use the following xpath to find the button in your test:'
               + locator)
    bullet2 = ('Notice that the XPath does not work. Change the space between '
               + "'My' and 'Button' to a non-breaking space."
               + ' This time the XPath should be valid.')
    btn_text = 'My Button'


class OverlappedElementConst(BaseConstants, PageConst):
    h3 = 'Overlapped Element'
    text = ('Entering text to a partially visible element may require '
            + 'scrolling it into view.')
    bullet1 = ('Record setting text into the Name input field (scroll element'
               + ' before entering the text).')
    bullet2 = ('Then execute your test to make sure that the text was entered'
               + ' correctly.')
    placeholder1 = 'Id'
    placeholder2 = 'Name'
    placeholder3 = 'Subject'


class ShadowDOMConst(BaseConstants, PageConst):
    h3 = 'Shadow DOM'
    text = ('This is a page with a Shadow DOM component guid-generator. Using '
            + 'it one can generate a guid and copy it to the clipboard.')
    bullet1 = ('Create a test that clicks on  and then on  buttons. This '
               + 'sequence of steps generates new guid and copies it to the '
               + 'clipboard.')
    bullet2 = ('Add an assertion step to your test to compare the value from '
               + 'the clipboard with the value of the input field.')
    bullet3 = ('Then execute the test to make sure that the assertion step is '
               + 'not failing.')
    h6 = 'GUID Generator:'


class AlertsConst(BaseConstants, PageConst):
    h3 = 'Alerts'
    text = ('Dealing with standard alerts, prompts and confirmations is an '
            + 'important skill in test automation.')
    bullet1 = ('Record clicks on `Alert`, `Confirm` and `Prompt` buttons. '
               + 'Click `OK` to confirm, answer with non-default value to the '
               + 'prompt.')
    bullet2 = ('Then execute your test to make sure that it passes completely'
               + ' without manual steps.')
    btn1 = 'Alert'
    btn2 = 'Confirm'
    btn3 = 'Prompt'
    alert_text = 'Today is a working day. Or less likely a holiday.'
    confirm_text = 'Today is Friday. Do you agree?'
    confirm_text_ok = 'Yes'
    confirm_text_cancel = 'No'
    prompt_text = """Choose "cats" or 'dogs'. Enter your value"""
    prompt_text_submit_format = 'User value: {}'
    prompt_text_cancel = prompt_text_submit_format.format('no answer')


class FileUploadConst(BaseConstants, PageConst):
    h3 = 'File Upload'
    text = ('Modern web applications often include file upload functionality, '
            + 'enabling users to easily share and manage documents, images, '
            + 'and other types of files directly from their devices, enhancing'
            + ' user interaction and content management.')
    bullet1 = 'Attach a file via drag&drop.'
    bullet2 = 'Attach a file using `Browse files` button'
    upload_title = 'Drag and drop your files here'
    upload_text = ('Limit 15MB per file. Supported files:'
                   + ' .PDF, .DOCX, .PPTX, .TXT, .XLSX')
    btn_text = 'Browse files'
    amount_format = '{} file(s) selected'

    # Test file settings
    file_name = 'sample.pdf'   # name of the installed file
    path_to_test_file = (
        Path(__file__).parent.parent / f'test_files/{file_name}')


class AnimatedButtonConst(BaseConstants, PageConst):
    h3 = 'Animated Button'
    text = ('Before clicking a button we may need to wait for it to become '
            + 'stable (not moving).')
    bullet1 = ('Record `Start Animation` button click. Wait for animation to '
               + 'complete and record click on `Moving Target`.')
    bullet2 = ('Then execute your test to make sure that when Moving Target is'
               + " clicked, it's class does not contain 'spin'. The class is "
               + 'printed on the status label below the buttons.')
    btn1_text = 'Start Animation'
    btn2_text = 'Moving Target'
    status_text_none = '---'
    status_text_action = 'Animating the button...'
    status_text_done = 'Animation done'
    status_text_format = "Moving Target clicked. It's class name is {}"
    status_text_action_clicked = status_text_format.format(
        "'btn btn-primary spin'")
    status_text_clicked = status_text_format.format("'btn btn-primary'")


class DisabledInputConst(BaseConstants, PageConst):
    h3 = 'Disabled Input'
    text = ('Sometimes elements become enabled after some time they are '
            + 'rendered on the page. A test should be able to wait for an '
            + 'element to become enabled.')
    bullet1 = 'Record button click. Also record text input into an edit field.'
    bullet2 = ('Make a test that enters text as soon as the edit field becomes'
               + ' enabled.')
    placeholder = 'Change me...'
    btn_text = 'Enable Edit Field with 5 seconds delay'
    status_text_none = '---'
    status_text_disabled = 'Input Disabled...'
    status_text_active = 'Input Enabled...'
