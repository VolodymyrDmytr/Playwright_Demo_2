from playwright.sync_api import Page, expect, Locator

from pages.base_page import BasePage
from config.locators import OverlappedElementLocators
from config.const import OverlappedElementConst


class OverlappedElementPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = OverlappedElementLocators(self.page)
        self.const = OverlappedElementConst()

    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        field1 = self.locators.fields_locator(1)
        field2 = self.locators.fields_locator(2)
        field3 = self.locators.fields_locator(3)

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(h4_2).to_have_text(self.const.h4_title2)
        expect(field1).to_have_attribute(
            'placeholder', self.const.placeholder1)
        expect(field2).to_have_attribute(
            'placeholder', self.const.placeholder2)
        expect(field3).to_have_attribute(
            'placeholder', self.const.placeholder3)

    def _field_locators(self) -> Locator:
        locator1 = self.locators.fields_locator(1)
        locator2 = self.locators.fields_locator(2)
        locator3 = self.locators.fields_locator(3)

        return locator1, locator2, locator3

    def fill_fields(
            self,
            ids: str,
            name: str,
            subject: str,
    ) -> bool:
        locator1, locator2, locator3 = self._field_locators()

        locator1.click()
        locator1.fill(ids)

        locator2.click()
        locator2.fill(name)

        locator3.click(force=True)
        locator3.fill(subject)

    def check_fields_data(
            self,
            ids: str,
            name: str,
            subject: str,
    ) -> bool:
        locator1, locator2, locator3 = self._field_locators()

        locator1.click()
        expect(locator1).to_have_value(ids)

        locator2.click()
        expect(locator2).to_have_value(name)

        locator3.click(force=True)
        expect(locator3).to_have_value(subject)
