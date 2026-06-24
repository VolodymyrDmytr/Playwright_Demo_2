from playwright.sync_api import Page, expect
import allure

from pages.base_page import BasePage
from config.locators import NonBreakingSpaceLocators
from config.const import NonBreakingSpaceConst


class NonBreakingSpacePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = NonBreakingSpaceLocators(self.page)
        self.const = NonBreakingSpaceConst()

    @allure.step('Verify page content is correct')
    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        locator = self.locators.locator_locator
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        btn = self.locators.button_locator

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(locator).to_have_text(self.const.locator)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(h4_2).to_have_text(self.const.h4_title2)
        expect(btn).to_have_text(self.const.btn_text)

    @allure.step('Click on button')
    def click_on_btn(self) -> None:
        locator = self.locators.button_locator
        locator.click()
