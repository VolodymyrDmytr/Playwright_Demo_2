import pytest
from playwright.sync_api import Page

# Import classes
from pages.home_page import HomePage
from pages.dynamic_id_page import DynamicIdPage
from pages.class_attribute_page import ClassAttributePage
from pages.hidden_layers_page import HiddenLayers
from pages.load_delays_page import LoadDelays
from pages.ajax_data import AjaxData
from pages.client_side_delay_page import ClientSideDelayPage
from pages.click_page import ClickPage
from pages.text_input_page import TextInputPage
from pages.scrollbars_page import ScrollbarsPage
from pages.dynamic_table_page import DynamicTablePage
from pages.verify_text_page import VerifyTextPage
from pages.progress_bar_page import ProgressBarPage


@pytest.fixture
def home_page(page: Page):
    home = HomePage(page)
    home.open_base_page()

    yield home


@pytest.fixture
def dynamic_page(page: Page):
    dynamic_page = DynamicIdPage(page)
    dynamic_page.open_base_page()
    dynamic_page.click_on_link('Dynamic ID')

    yield dynamic_page


@pytest.fixture
def class_attr(page: Page):
    class_attr = ClassAttributePage(page)
    class_attr.open_base_page()
    class_attr.click_on_link('Class Attribute')

    yield class_attr


@pytest.fixture
def hidden(page: Page):
    hidden = HiddenLayers(page)
    hidden.open_base_page()
    hidden.click_on_link('Hidden Layers')

    yield hidden


@pytest.fixture
def load(page: Page):
    load = LoadDelays(page)
    load.open_base_page()
    load.click_on_link('Load Delay')

    yield load


@pytest.fixture
def ajax(page: Page):
    ajax = AjaxData(page)
    ajax.open_base_page()
    ajax.click_on_link('AJAX Data')

    yield ajax


@pytest.fixture
def delay(page: Page):
    delay = ClientSideDelayPage(page)
    delay.open_base_page()
    delay.click_on_link('Client Side Delay')

    yield delay


@pytest.fixture
def click(page: Page):
    click = ClickPage(page)
    click.open_base_page()
    click.click_on_link('Click')

    yield click


@pytest.fixture
def text(page: Page):
    text = TextInputPage(page)
    text.open_base_page()
    text.click_on_link('Text Input')

    yield text


@pytest.fixture
def scroll(page: Page):
    scroll = ScrollbarsPage(page)
    scroll.open_base_page()
    scroll.click_on_link('Scrollbars')

    yield scroll


@pytest.fixture
def table(page: Page):
    scroll = DynamicTablePage(page)
    scroll.open_base_page()
    scroll.click_on_link('Dynamic Table')

    yield scroll


@pytest.fixture
def verify(page: Page):
    verify = VerifyTextPage(page)
    verify.open_base_page()
    verify.click_on_link('Verify Text')

    yield verify


@pytest.fixture
def progress(page: Page):
    progress = ProgressBarPage(page)
    progress.open_base_page()
    progress.click_on_link('Progress Bar')

    yield progress
