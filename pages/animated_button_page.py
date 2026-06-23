from playwright.async_api import Page, expect

from pages.base_page import BasePage
from config.locators import AnimatedButtonLocator
from config.const import AnimatedButtonConst


class AnimatedButtonPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = AnimatedButtonLocator(self.page)
        self.const = AnimatedButtonConst()

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        btn1 = self.locators.start_btn_locator
        btn2 = self.locators.target_btn_locator

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.text)
        await expect(h4_1).to_have_text(self.const.h4_title1)
        await expect(bullet1).to_have_text(self.const.bullet1)
        await expect(bullet2).to_have_text(self.const.bullet2)
        await expect(h4_2).to_have_text(self.const.h4_title2)
        await expect(btn1).to_have_text(self.const.btn1_text)
        await expect(btn2).to_have_text(self.const.btn2_text)

    async def check_status_text(
            self,
            status: str,
    ) -> bool:
        """Checks is status text as expected

        Args:
            status (str):
            default / done / moving / clicked move / clicked static

        Returns:
            bool: True, if status text is as expected
        """
        locator = self.locators.status_text_locator
        status = status.lower().strip()

        if status == 'default':
            text = self.const.status_text_none
        elif status == 'done':
            text = self.const.status_text_done
        elif status == 'moving':
            text = self.const.status_text_action
        elif status == 'clicked move':
            text = self.const.status_text_action_clicked
        elif status == 'clicked static':
            text = self.const.status_text_clicked
        else:
            text = ''

        await expect(locator).to_have_text(text, timeout=6000)

    async def click_on_start_btn(self) -> None:
        locator = self.locators.start_btn_locator
        await locator.click()

    async def click_on_target_btn(self) -> None:
        locator = self.locators.target_btn_locator
        await locator.click()
