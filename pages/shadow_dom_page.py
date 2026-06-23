from playwright.async_api import Page, expect
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

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        bullet3 = self.locators.bullet_locators(3)
        h6 = self.locators.h6_locator

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.text)
        await expect(bullet1).to_have_text(self.const.bullet1)
        await expect(bullet2).to_have_text(self.const.bullet2)
        await expect(bullet3).to_have_text(self.const.bullet3)
        await expect(h6).to_have_text(self.const.h6)

    async def click_generate_guid(self) -> None:
        locator = self.locators.generate_btn_locator
        await locator.click()

    # Error in console after click on page
    async def copy_guid_btn(self) -> str:
        locator = self.locators.copy_btn_locator
        await locator.click()

    async def check_guid_field(
            self,
            data: str,
    ) -> bool:
        locator = self.locators.field_locator
        await expect(locator).to_have_value(data)

    async def get_generated_guid(self) -> str:
        locator = self.locators.field_locator
        data = await locator.input_value()
        logger.debug('Generated GUID: %s', data)
        return data

    async def check_field_is_not_empty(self) -> bool:
        locator = self.locators.field_locator
        await expect(locator).not_to_have_value('')
