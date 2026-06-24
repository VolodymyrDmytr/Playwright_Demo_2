from playwright.sync_api import Page, expect
import allure

from pages.base_page import BasePage
from config.locators import DisabledInputLocators
from config.const import DisabledInputConst


class DisabledInputPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = DisabledInputLocators(self.page)
        self.const = DisabledInputConst()
        self.timeout = 6000

    @allure.step('Verify page content is correct')
    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        field = self.locators.field_locator
        btn = self.locators.btn_locator

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(h4_2).to_have_text(self.const.h4_title2)
        expect(field).to_have_attribute('placeholder', self.const.placeholder)
        expect(btn).to_have_text(self.const.btn_text)

    @allure.step('Check is status text correspond to {status} status')
    def check_status_text(
            self,
            status: str,
    ) -> bool:
        """Checks status text

        Args:
            status (str): default / disabled / active

        Returns:
            bool: True, if status text is as expected
        """
        locator = self.locators.status_text_locator
        status = status.lower().strip()

        if status == 'default':
            text = self.const.status_text_none
        elif status == 'disabled':
            text = self.const.status_text_disabled
        elif status == 'active':
            text = self.const.status_text_active
        else:
            text = ''

        expect(locator).to_have_text(text, timeout=self.timeout)

    @allure.step('Fill field with data: {data}')
    def fill_field(
            self,
            data: str,
    ) -> None:
        locator = self.locators.field_locator
        locator.fill(data, timeout=self.timeout)

    @allure.step('Check is field disabled')
    def check_is_field_disabled(self) -> bool:
        locator = self.locators.field_locator
        expect(locator).to_be_disabled()

    @allure.step('Check is field contain data: {data}')
    def check_field_data(
            self,
            data: str,
    ) -> bool:
        locator = self.locators.field_locator
        expect(locator).to_have_value(data)

    @allure.step('Click on button')
    def click_on_btn(self) -> None:
        locator = self.locators.btn_locator
        locator.click()
