from playwright.async_api import Page, expect

from pages.base_page import BasePage
from config.locators import DisabledInputLocators
from config.const import DisabledInputConst


class DisabledInputPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = DisabledInputLocators(self.page)
        self.const = DisabledInputConst()
        self.timeout = 6000

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        field = self.locators.field_locator
        btn = self.locators.btn_locator

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.text)
        await expect(h4_1).to_have_text(self.const.h4_title1)
        await expect(bullet1).to_have_text(self.const.bullet1)
        await expect(bullet2).to_have_text(self.const.bullet2)
        await expect(h4_2).to_have_text(self.const.h4_title2)
        await expect(field).to_have_attribute('placeholder',
                                              self.const.placeholder)
        await expect(btn).to_have_text(self.const.btn_text)

    async def check_status_text(
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

        await expect(locator).to_have_text(text, timeout=self.timeout)

    async def fill_field(
            self,
            data: str,
    ) -> None:
        locator = self.locators.field_locator
        await locator.fill(data, timeout=self.timeout)

    async def check_is_field_disabled(self) -> bool:
        locator = self.locators.field_locator
        await expect(locator).to_be_disabled()

    async def check_field_data(
            self,
            data: str,
    ) -> bool:
        locator = self.locators.field_locator
        await expect(locator).to_have_value(data)

    async def click_on_btn(self) -> None:
        locator = self.locators.btn_locator
        await locator.click()
