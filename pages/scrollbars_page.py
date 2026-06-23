from playwright.async_api import Page, expect


from pages.base_page import BasePage
from config.locators import ScrollbarsLocators
from config.const import ScrollbarsConst


class ScrollbarsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ScrollbarsLocators(self.page)
        self.const = ScrollbarsConst()

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        btn = self.locators.btn_locator

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.text)
        await expect(h4_1).to_have_text(self.const.h4_title1)
        await expect(bullet1).to_have_text(self.const.bullet1)
        await expect(bullet2).to_have_text(self.const.bullet2)
        await expect(h4_2).to_have_text(self.const.h4_title2)
        await expect(btn).to_have_text(self.const.btn_text)

    async def click_on_button(self) -> None:
        locator = self.locators.btn_locator
        await locator.click()
