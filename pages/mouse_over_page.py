from playwright.async_api import Page, expect, Locator

from pages.base_page import BasePage
from config.locators import MouseOverLocators
from config.const import MouseOverConst


class MouseOverPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = MouseOverLocators(self.page)
        self.const = MouseOverConst()

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text1 = self.locators.text_locators(1)
        text2 = self.locators.text_locators(2)
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        text3 = self.locators.text_locators(3)
        text5 = self.locators.text_locators(5)

        await expect(h3).to_have_text(self.const.h3)
        await expect(text1).to_have_text(self.const.text1)
        await expect(text2).to_have_text(self.const.text2)
        await expect(h4_1).to_have_text(self.const.h4_title1)
        await expect(bullet1).to_have_text(self.const.bullet1)
        await expect(bullet2).to_have_text(self.const.bullet2)
        await expect(h4_2).to_have_text(self.const.h4_title2)
        await expect(text3).to_have_text(self.const.text3)
        await expect(text5).to_have_text(self.const.text5)

    async def click_on_link_p(
            self,
            data: int,
            clicks_amount: int,
    ) -> None:
        """Click on one of the links

        Args:
            data (int): 1 / 2
        """
        active_link = self.locators.link_page_locator(data)
        hover_link = self.locators.link_on_hover_locator

        await active_link.hover()

        for _ in range(0, clicks_amount):
            await hover_link.click()

    async def check_amount_of_clicks_for_link(
            self,
            data: int,
            clicks_amount: int,
    ) -> bool:
        if data == 1:
            data = self.const.text4_counter.format(clicks_amount)
            locator = self.locators.text_locators(4)
        elif data == 2:
            data = self.const.text6_counter.format(clicks_amount)
            locator = self.locators.text_locators(6)
        else:
            data = ''
            locator = Locator()

        await expect(locator).to_have_text(data)
