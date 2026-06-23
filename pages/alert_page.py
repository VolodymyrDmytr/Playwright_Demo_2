from playwright.async_api import Page, expect

from pages.base_page import BasePage
from config.locators import AlertsLocators
from config.const import AlertsConst


class AlertsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = AlertsLocators(self.page)
        self.const = AlertsConst()

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        btn1 = self.locators.alert_btn_locator
        btn2 = self.locators.confirm_btn_locator
        btn3 = self.locators.prompt_btn_locator

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.text)
        await expect(h4_1).to_have_text(self.const.h4_title1)
        await expect(bullet1).to_have_text(self.const.bullet1)
        await expect(bullet2).to_have_text(self.const.bullet2)
        await expect(h4_2).to_have_text(self.const.h4_title2)
        await expect(btn1).to_have_text(self.const.btn1)
        await expect(btn2).to_have_text(self.const.btn2)
        await expect(btn3).to_have_text(self.const.btn3)

    async def click_alert_btn(self) -> None:
        locator = self.locators.alert_btn_locator
        await locator.click()

    async def click_confirm_btn(self) -> None:
        locator = self.locators.confirm_btn_locator
        await locator.click()

    async def click_prompt_btn(self) -> None:
        locator = self.locators.prompt_btn_locator
        await locator.click()

    async def accept_dialog(self) -> None:
        await self.page.on('dialog', lambda d: d.accept())

    async def cancel_dialog(self) -> None:
        await self.page.on('dialog', lambda d: d.dismiss())

    def _assert_dialog_text(
            self,
            dialog,
            text: str,
    ) -> bool:
        assert dialog.message == text

    async def check_dialog_text(
            self,
            text: str,
    ) -> bool:
        await self.page.on('dialog', lambda d: self._assert_dialog_text(
            d, text))

    async def accept_prompt(
            self,
            data: str,
    ) -> None:
        await self.page.on('dialog', lambda d: d.accept(data))

    async def cancel_prompt(
            self,
            data: str,
    ) -> None:
        await self.page.on('dialog', lambda d: d.dismiss(data))
