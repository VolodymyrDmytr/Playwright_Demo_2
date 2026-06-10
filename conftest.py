import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.dynamic_id_page import DynamicIdPage
from pages.class_attribute_page import ClassAttributePage
from pages.hidden_layers_page import HiddenLayers
from pages.load_delays_page import LoadDelays


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
