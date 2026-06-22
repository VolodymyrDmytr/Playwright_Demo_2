import pytest
from playwright.sync_api import Page

# Support method
from config.file_installer import install_file_if_it_is_not_exist as file_inst

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
from pages.visibility_page import VisibilityPage
from pages.sample_app_page import SampleAppPage
from pages.mouse_over_page import MouseOverPage
from pages.non_breaking_space_page import NonBreakingSpacePage
from pages.overlapped_element_page import OverlappedElementPage
from pages.shadow_dom_page import ShadowDOMPage
from pages.alert_page import AlertsPage
from pages.file_upload_page import FileUploadPage
from pages.animated_button_page import AnimatedButtonPage
from pages.disabled_input_page import DisabledInputPage
from pages.auto_wait_page import AutoWaitPage
from pages.frames_page import FramesPage


@pytest.fixture
def home_page(page: Page) -> object:
    home = HomePage(page)
    home.open_base_page()

    yield home


@pytest.fixture
def dynamic_page(page: Page) -> object:
    dynamic_page = DynamicIdPage(page)
    dynamic_page.open_base_page()
    dynamic_page.click_on_link('Dynamic ID')

    yield dynamic_page


@pytest.fixture
def class_attr(page: Page) -> object:
    class_attr = ClassAttributePage(page)
    class_attr.open_base_page()
    class_attr.click_on_link('Class Attribute')

    yield class_attr


@pytest.fixture
def hidden(page: Page) -> object:
    hidden = HiddenLayers(page)
    hidden.open_base_page()
    hidden.click_on_link('Hidden Layers')

    yield hidden


@pytest.fixture
def load(page: Page) -> object:
    load = LoadDelays(page)
    load.open_base_page()
    load.click_on_link('Load Delay')

    yield load


@pytest.fixture
def ajax(page: Page) -> object:
    ajax = AjaxData(page)
    ajax.open_base_page()
    ajax.click_on_link('AJAX Data')

    yield ajax


@pytest.fixture
def delay(page: Page) -> object:
    delay = ClientSideDelayPage(page)
    delay.open_base_page()
    delay.click_on_link('Client Side Delay')

    yield delay


@pytest.fixture
def click(page: Page) -> object:
    click = ClickPage(page)
    click.open_base_page()
    click.click_on_link('Click')

    yield click


@pytest.fixture
def text(page: Page) -> object:
    text = TextInputPage(page)
    text.open_base_page()
    text.click_on_link('Text Input')

    yield text


@pytest.fixture
def scroll(page: Page) -> object:
    scroll = ScrollbarsPage(page)
    scroll.open_base_page()
    scroll.click_on_link('Scrollbars')

    yield scroll


@pytest.fixture
def table(page: Page) -> object:
    scroll = DynamicTablePage(page)
    scroll.open_base_page()
    scroll.click_on_link('Dynamic Table')

    yield scroll


@pytest.fixture
def verify(page: Page) -> object:
    verify = VerifyTextPage(page)
    verify.open_base_page()
    verify.click_on_link('Verify Text')

    yield verify


@pytest.fixture
def progress(page: Page) -> object:
    progress = ProgressBarPage(page)
    progress.open_base_page()
    progress.click_on_link('Progress Bar')

    yield progress


@pytest.fixture
def visibility(page: Page) -> object:
    visibility = VisibilityPage(page)
    visibility.open_base_page()
    visibility.click_on_link('Visibility')

    yield visibility


@pytest.fixture
def app(page: Page) -> object:
    app = SampleAppPage(page)
    app.open_base_page()
    app.click_on_link('Sample App')

    yield app


@pytest.fixture
def mouse(page: Page) -> object:
    mouse = MouseOverPage(page)
    mouse.open_base_page()
    mouse.click_on_link('Mouse Over')

    yield mouse


@pytest.fixture
def nbsp(page: Page) -> object:
    nbsp = NonBreakingSpacePage(page)
    nbsp.open_base_page()
    nbsp.click_on_link('Non-Breaking Space')

    yield nbsp


@pytest.fixture
def overlapped(page: Page) -> object:
    overlapped = OverlappedElementPage(page)
    overlapped.open_base_page()
    overlapped.click_on_link('Overlapped Element')

    yield overlapped


@pytest.fixture
def shadow_dom(page: Page) -> object:
    shadow_dom = ShadowDOMPage(page)
    shadow_dom.open_base_page()
    shadow_dom.click_on_link('Shadow DOM')

    yield shadow_dom


@pytest.fixture
def alerts(page: Page) -> object:
    alerts = AlertsPage(page)
    alerts.open_base_page()
    alerts.click_on_link('Alerts')

    yield alerts


@pytest.fixture
def upload(page: Page) -> object:
    file_inst()

    upload = FileUploadPage(page)
    upload.open_base_page()
    upload.click_on_link('File Upload')

    yield upload


@pytest.fixture
def animated(page: Page) -> object:
    animated = AnimatedButtonPage(page)
    animated.open_base_page()
    animated.click_on_link('Animated Button')

    yield animated


@pytest.fixture
def disabled(page: Page) -> object:
    disabled = DisabledInputPage(page)
    disabled.open_base_page()
    disabled.click_on_link('Disabled Input')

    yield disabled


@pytest.fixture
def wait(page: Page) -> object:
    wait = AutoWaitPage(page)
    wait.open_base_page()
    wait.click_on_link('Auto Wait')

    yield wait


@pytest.fixture
def iframe(page: Page) -> object:
    iframe = FramesPage(page)
    iframe.open_base_page()
    iframe.click_on_link('Frames')

    yield iframe
