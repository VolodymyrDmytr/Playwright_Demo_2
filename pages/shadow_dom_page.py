from playwright.sync_api import Page, expect
import logging

from pages.base_page import BasePage
from config.locators import ShadowDOMLocators
from config.const import ShadowDOMConst

logger = logging.getLogger(__name__)


class ShadowDOMPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ShadowDOMLocators(self.page)
        self.const = ShadowDOMConst()

    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        bullet3 = self.locators.bullet_locators(3)
        h6 = self.locators.h6_locator

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(bullet3).to_have_text(self.const.bullet3)
        expect(h6).to_have_text(self.const.h6)

    def click_generate_guid(self) -> None:
        locator = self.locators.generate_btn_locator
        locator.click()

    # Error in console after click on page
    def copy_guid_btn(self) -> str:
        locator = self.locators.copy_btn_locator
        locator.click()

    def check_guid_field(
            self,
            data: str,
    ) -> bool:
        locator = self.locators.field_locator
        expect(locator).to_have_value(data)

    def get_generated_guid(self) -> str:
        locator = self.locators.field_locator
        data = locator.input_value()
        logger.debug('Generated GUID: %s', data)
        return data

    def check_field_is_not_empty(self) -> bool:
        locator = self.locators.field_locator
        expect(locator).not_to_have_value('')
