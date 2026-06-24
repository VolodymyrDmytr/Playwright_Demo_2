from playwright.sync_api import Page, expect
import allure

from pages.base_page import BasePage
from config.locators import AlertsLocators
from config.const import AlertsConst


class AlertsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = AlertsLocators(self.page)
        self.const = AlertsConst()

    @allure.step('Verify page content is correct')
    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        btn1 = self.locators.alert_btn_locator
        btn2 = self.locators.confirm_btn_locator
        btn3 = self.locators.prompt_btn_locator

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(h4_2).to_have_text(self.const.h4_title2)
        expect(btn1).to_have_text(self.const.btn1)
        expect(btn2).to_have_text(self.const.btn2)
        expect(btn3).to_have_text(self.const.btn3)

    @allure.step('Click on Alert button')
    def click_alert_btn(self) -> None:
        locator = self.locators.alert_btn_locator
        locator.click()

    @allure.step('Click on Confirm button')
    def click_confirm_btn(self) -> None:
        locator = self.locators.confirm_btn_locator
        locator.click()

    @allure.step('Click on Prompt button')
    def click_prompt_btn(self) -> None:
        locator = self.locators.prompt_btn_locator
        locator.click()

    @allure.step('Accept dialog')
    def accept_dialog(self) -> None:
        self.page.on('dialog', lambda d: d.accept())

    @allure.step('Cancel dialog')
    def cancel_dialog(self) -> None:
        self.page.on('dialog', lambda d: d.dismiss())

    def _assert_dialog_text(
            self,
            dialog,
            text: str,
    ) -> bool:
        assert dialog.message == text

    @allure.step('Check is dialog text {text}')
    def check_dialog_text(
            self,
            text: str,
    ) -> bool:
        self.page.on('dialog', lambda d: self._assert_dialog_text(d, text))

    @allure.step('Accept prompt')
    def accept_prompt(
            self,
            data: str,
    ) -> None:
        self.page.on('dialog', lambda d: d.accept(data))

    @allure.step('Canceling prompt')
    def cancel_prompt(
            self,
            data: str,
    ) -> None:
        self.page.on('dialog', lambda d: d.dismiss(data))
