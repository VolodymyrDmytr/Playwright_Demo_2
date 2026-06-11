from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from config.locators import TextInputLocators
from config.const import TextInputConst


class TextInputPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = TextInputLocators(self.page)
        self.const = TextInputConst()

    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        field_title = self.locators.field_name_locator
        field = self.locators.field_locator
        btn = self.locators.btn_locator

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(h4_2).to_have_text(self.const.h4_title2)
        expect(field_title).to_have_text(self.const.field_title)
        expect(field).to_have_attribute(
            'placeholder', self.const.field_placeholder)
        expect(btn).to_have_text(self.const.btn_text)

    def change_button_name(
            self,
            data: str,
    ) -> bool:
        field_locator = self.locators.field_locator
        btn_locator = self.locators.btn_locator

        field_locator.fill(data)
        btn_locator.click()
        expect(btn_locator).to_have_text(data)
