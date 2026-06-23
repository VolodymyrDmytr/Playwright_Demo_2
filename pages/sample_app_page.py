from playwright.async_api import Page, expect

from pages.base_page import BasePage
from config.locators import SampleAppLocators
from config.const import SampleAppConst


class SampleAppPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = SampleAppLocators(self.page)
        self.const = SampleAppConst()

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        btn = self.locators.btn_locator

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.text)
        await expect(btn).to_have_text(self.const.btn_text)

    async def fill_form(
            self,
            name: str,
            password: str,
    ) -> None:
        name_locator = self.locators.name_field_locator
        password_locator = self.locators.passwrd_locator

        await name_locator.fill(name)
        await password_locator.fill(password)

    async def click_on_btn(self) -> None:
        locator = self.locators.btn_locator
        await locator.click()

    async def check_info_text_default_error(
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

        await expect(locator).to_have_text(expected_text)

    async def check_success_info_text(
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
        await expect(locator).to_have_text(
            self.const.info_text_success.format(data))
