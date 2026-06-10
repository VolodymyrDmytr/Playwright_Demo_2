from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from config.locators import HiddenLayersLocators
from config.const import HiddenLayersConst


class HiddenLayers(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = HiddenLayersLocators(self.page)
        self.const = HiddenLayersConst()

    def check_page_content(self) -> bool:
        h3 = self.locators.h3_title_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullets_locator(1)
        bullet2 = self.locators.bullets_locator(2)
        h4_2 = self.locators.h4_title_locator(2)
        btn = self.locators.btn_locator

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(h4_2).to_have_text(self.const.h4_title2)
        expect(btn).to_have_text(self.const.btn_text)

    def click_on_button(self) -> None:
        locator = self.locators.btn_locator
        locator.click()

    def check_is_success(self) -> bool:
        locator = self.locators.success_locator
        expect(locator).to_have_attribute('style', 'z-index: 2;')
