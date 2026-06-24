from playwright.sync_api import Page, expect
import allure

from pages.base_page import BasePage
from config.locators import SampleAppLocators
from config.const import SampleAppConst


class SampleAppPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = SampleAppLocators(self.page)
        self.const = SampleAppConst()

    @allure.step('Verify page content is correct')
    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        btn = self.locators.btn_locator

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(btn).to_have_text(self.const.btn_text)

    @allure.step('Fill form, name({name}) and password({password})')
    def fill_form(
            self,
            name: str,
            password: str,
    ) -> None:
        name_locator = self.locators.name_field_locator
        password_locator = self.locators.passwrd_locator

        name_locator.fill(name)
        password_locator.fill(password)

    @allure.step('Click on Apply button')
    def click_on_btn(self) -> None:
        locator = self.locators.btn_locator
        locator.click()

    @allure.step('Check {data} info text')
    def check_info_text_default_error(
            self,
            data: str,
    ) -> bool:
        """Checks default or error info texts

        Args:
            data (str): default / error

        Returns:
            bool: True, if info text is as expected
        """
        data = data.lower()

        locator = self.locators.info_text_locator

        if data == 'default':
            expected_text = self.const.info_text_default
        elif data == 'error':
            expected_text = self.const.info_text_error
        else:
            expected_text = ''

        expect(locator).to_have_text(expected_text)

    @allure.step('Check success info text')
    def check_success_info_text(
            self,
            data: str,
    ) -> bool:
        """Checks success info text

        Args:
            data (str): name, that was filled in the name field

        Returns:
            bool: True, if success info text is as expected
        """
        locator = self.locators.info_text_locator
        expect(locator).to_have_text(self.const.info_text_success.format(data))
