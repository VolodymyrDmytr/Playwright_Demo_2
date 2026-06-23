from playwright.async_api import Page, expect

from pages.base_page import BasePage
from config.const import DynamicIdConst
from config.locators import DynamicIdLoators


class DynamicIdPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = DynamicIdLoators(self.page)
        self.const = DynamicIdConst()

    async def check_page_text(self) -> bool:
        h3_locator = self.locators.h3_locator
        text_locator = self.locators.text_locator
        h4_1st_locator = self.locators.h4_title_locator(1)
        h4_2nd_locator = self.locators.h4_title_locator(2)
        bullet_1st = self.locators.bullet_locators(1)
        bullet_2nd = self.locators.bullet_locators(2)
        btn = self.locators.button_locator

        await expect(h3_locator).to_have_text(self.const.h3_title)
        await expect(text_locator).to_have_text(self.const.text)
        await expect(h4_1st_locator).to_have_text(self.const.h4_title1)
        await expect(h4_2nd_locator).to_have_text(self.const.h4_title2)
        await expect(bullet_1st).to_have_text(self.const.bullet1)
        await expect(bullet_2nd).to_have_text(self.const.bullet2)
        await expect(btn).to_have_text(self.const.btn_text)

    async def click_on_btn(self) -> None:
        await self.locators.button_locator.click()
