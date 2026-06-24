from playwright.sync_api import Page, expect, Locator
import allure

from pages.base_page import BasePage
from config.locators import FramesLocators
from config.const import FramesConst


class FramesPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = FramesLocators(self.page)
        self.const = FramesConst()

    @allure.step('Verify page content is correct')
    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1_1 = self.locators.bullet_locators(1)
        bullet1_2 = self.locators.bullet_locators(2)
        bullet1_3 = self.locators.bullet_locators(3)
        bullet1_4 = self.locators.bullet_locators(4)
        h4_2 = self.locators.h4_title_locator(2)
        bullet2_1 = self.locators.bullet_locators(5)
        bullet2_2 = self.locators.bullet_locators(6)
        bullet2_3 = self.locators.bullet_locators(7)
        bullet2_4 = self.locators.bullet_locators(8)
        h4_3 = self.locators.h4_title_locator(3)
        btn1_1 = self.locators.edit_btn_1_locator
        btn1_2 = self.locators.submit_btn_1_locator
        btn1_3 = self.locators.click_btn_1_locator
        btn1_4 = self.locators.primary_btn_1_locator
        btn2_1 = self.locators.edit_btn_2_locator
        btn2_2 = self.locators.submit_btn_2_locator
        btn2_3 = self.locators.click_btn_2_locator
        btn2_4 = self.locators.primary_btn_2_locator

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1_1).to_have_text(self.const.bullet1_1)
        expect(bullet1_2).to_have_text(self.const.bullet1_2)
        expect(bullet1_3).to_have_text(self.const.bullet1_3)
        expect(bullet1_4).to_have_text(self.const.bullet1_4)
        expect(h4_2).to_have_text(self.const.h4_title2)
        expect(bullet2_1).to_have_text(self.const.bullet2_1)
        expect(bullet2_2).to_have_text(self.const.bullet2_2)
        expect(bullet2_3).to_have_text(self.const.bullet2_3)
        expect(bullet2_4).to_have_text(self.const.bullet2_4)
        expect(h4_3).to_have_text(self.const.h4_title3)
        expect(btn1_1).to_have_text(self.const.btn1)
        expect(btn1_2).to_have_text(self.const.btn2)
        expect(btn1_3).to_have_text(self.const.btn3)
        expect(btn1_4).to_have_text(self.const.btn4)
        expect(btn2_1).to_have_text(self.const.btn1)
        expect(btn2_2).to_have_text(self.const.btn2)
        expect(btn2_3).to_have_text(self.const.btn3)
        expect(btn2_4).to_have_text(self.const.btn4)

    def _iframe_locator(
            self,
            iframe: int,
            locator1: Locator,
            locator2: Locator,
    ) -> Locator:
        if iframe == 1:
            return locator1
        elif iframe == 2:
            return locator2
        else:
            return Locator()

    @allure.step('Check that status text is not visible')
    def check_status_text_is_not_shown(
            self,
            iframe: int,
    ) -> bool:
        locator = self._iframe_locator(
            iframe,
            self.locators.status_text_1_locator,
            self.locators.status_text_2_locator)
        expect(locator).to_contain_text('')

    @allure.step('Check is status text in iframe {iframe} has {btn_text}')
    def check_status_text(
            self,
            iframe: int,
            btn_text: str,
    ) -> bool:
        locator = self._iframe_locator(
            iframe,
            self.locators.status_text_1_locator,
            self.locators.status_text_2_locator)
        txt = self.const.status_text_format.format(btn_text)

        expect(locator).to_have_text(txt)

    @allure.step('Click on Edit button in iframe {iframe}')
    def click_on_edit_btn(
            self,
            iframe: int,
    ) -> None:
        locator = self._iframe_locator(
            iframe,
            self.locators.edit_btn_1_locator,
            self.locators.edit_btn_2_locator)
        locator.click()

    @allure.step('Click on Submit button in iframe {iframe}')
    def click_on_submit_btn(
            self,
            iframe: int,
    ) -> None:
        locator = self._iframe_locator(
            iframe,
            self.locators.submit_btn_1_locator,
            self.locators.submit_btn_2_locator)
        locator.click()

    @allure.step('Click on Click me button in iframe {iframe}')
    def click_on_click_btn(
            self,
            iframe: int,
    ) -> None:
        locator = self._iframe_locator(
            iframe,
            self.locators.click_btn_1_locator,
            self.locators.click_btn_2_locator)
        locator.click()

    @allure.step('Click on Primary button in iframe {iframe}')
    def click_on_primary_btn(
            self,
            iframe: int,
    ) -> None:
        locator = self._iframe_locator(
            iframe,
            self.locators.primary_btn_1_locator,
            self.locators.primary_btn_2_locator)
        locator.click()
