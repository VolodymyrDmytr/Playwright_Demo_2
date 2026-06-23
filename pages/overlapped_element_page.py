from playwright.async_api import Page, expect, Locator

from pages.base_page import BasePage
from config.locators import OverlappedElementLocators
from config.const import OverlappedElementConst


class OverlappedElementPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = OverlappedElementLocators(self.page)
        self.const = OverlappedElementConst()

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        field1 = self.locators.fields_locator(1)
        field2 = self.locators.fields_locator(2)
        field3 = self.locators.fields_locator(3)

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.text)
        await expect(h4_1).to_have_text(self.const.h4_title1)
        await expect(bullet1).to_have_text(self.const.bullet1)
        await expect(bullet2).to_have_text(self.const.bullet2)
        await expect(h4_2).to_have_text(self.const.h4_title2)
        await expect(field1).to_have_attribute(
            'placeholder', self.const.placeholder1)
        await expect(field2).to_have_attribute(
            'placeholder', self.const.placeholder2)
        await expect(field3).to_have_attribute(
            'placeholder', self.const.placeholder3)

    def _field_locators(self) -> Locator:
        locator1 = self.locators.fields_locator(1)
        locator2 = self.locators.fields_locator(2)
        locator3 = self.locators.fields_locator(3)

        return locator1, locator2, locator3

    async def fill_fields(
            self,
            ids: str,
            name: str,
            subject: str,
    ) -> bool:
        locator1, locator2, locator3 = self._field_locators()

        await locator1.click()
        await locator1.fill(ids)

        await locator2.click()
        await locator2.fill(name)

        await locator3.click(force=True)
        await locator3.fill(subject)

    async def check_fields_data(
            self,
            ids: str,
            name: str,
            subject: str,
    ) -> bool:
        locator1, locator2, locator3 = self._field_locators()

        await locator1.click()
        await expect(locator1).to_have_value(ids)

        await locator2.click()
        await expect(locator2).to_have_value(name)

        await locator3.click(force=True)
        await expect(locator3).to_have_value(subject)
