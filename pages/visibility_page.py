from playwright.async_api import Page, expect, Locator   # , TimeoutError
import playwright.async_api

from pages.base_page import BasePage
from config.locators import VisibilityLocators
from config.const import VisibilityConst


class VisibilityPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = VisibilityLocators(self.page)
        self.const = VisibilityConst()

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        bullet1_1 = self.locators.bullet_locators(1)
        bullet1_2 = self.locators.bullet_locators(2)
        bullet1_3 = self.locators.bullet_locators(3)
        bullet1_4 = self.locators.bullet_locators(4)
        bullet1_5 = self.locators.bullet_locators(5)
        h4_1 = self.locators.h4_title_locator(1)
        bullet2_1 = self.locators.bullet_locators(6)
        bullet2_2 = self.locators.bullet_locators(7)
        bullet2_3 = self.locators.bullet_locators(8)
        h4_2 = self.locators.h4_title_locator(2)
        btn_blue = self.locators.blue_btn_locator
        btn_red = self.locators.red_btn_locator
        btn_yellow = self.locators.yellow_btn_locator
        btn_green = self.locators.green_btn_locator
        btn_info1 = self.locators.info_btns_locator(1)
        btn_info2 = self.locators.info_btns_locator(2)
        btn_info3 = self.locators.info_btns_locator(3)
        btn_info4 = self.locators.info_btns_locator(4)

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.txt)
        await expect(bullet1_1).to_have_text(self.const.bullets1_1)
        await expect(bullet1_2).to_have_text(self.const.bullets1_2)
        await expect(bullet1_3).to_have_text(self.const.bullets1_3)
        await expect(bullet1_4).to_have_text(self.const.bullets1_4)
        await expect(bullet1_5).to_have_text(self.const.bullets1_5)
        await expect(h4_1).to_have_text(self.const.h4_title1)
        await expect(bullet2_1).to_have_text(self.const.bullets2_1)
        await expect(bullet2_2).to_have_text(self.const.bullets2_2)
        await expect(bullet2_3).to_have_text(self.const.bullets2_3)
        await expect(h4_2).to_have_text(self.const.h4_title2)
        await expect(btn_blue).to_have_text(self.const.btn_blue)
        await expect(btn_red).to_have_text(self.const.btn_red)
        await expect(btn_yellow).to_have_text(self.const.btn_yellow)
        await expect(btn_green).to_have_text(self.const.btn_green)
        await expect(btn_info1).to_have_text(self.const.btn_info_1)
        await expect(btn_info2).to_have_text(self.const.btn_info_2)
        await expect(btn_info3).to_have_text(self.const.btn_info_3)
        await expect(btn_info4).to_have_text(self.const.btn_info_4)

    async def click_hide_btn(self) -> None:
        locator = self.locators.blue_btn_locator
        await locator.click()

    async def check_are_buttons_in_correct_visibility(self) -> bool:
        hide = self.locators.blue_btn_locator
        removed = self.locators.red_btn_locator
        zero_width = self.locators.yellow_btn_locator
        overlapped = self.locators.green_btn_locator
        info1 = self.locators.info_btns_locator(1)
        info2 = self.locators.info_btns_locator(2)
        info3 = self.locators.info_btns_locator(3)
        info4 = self.locators.info_btns_locator(4)

        await expect(hide).to_be_visible()
        await expect(removed).not_to_be_visible()
        await expect(zero_width).not_to_be_visible()
        await self._try_click_overlapped(overlapped)
        await self._try_click_overlapped(info1)
        await expect(info2).not_to_be_visible()
        await expect(info3).not_to_be_visible()
        await self._try_click_overlapped(info4)

    async def _try_click_overlapped(
            self,
            data: Locator,
    ) -> bool:
        try:
            await data.click(trial=True, timeout=2000)
        except playwright.async_api.TimeoutError:
            return True
        else:
            return False
