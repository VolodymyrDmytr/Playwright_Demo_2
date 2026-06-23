from playwright.async_api import Page, expect
import playwright.async_api

from pages.base_page import BasePage
from config.locators import AutoWaitLocators
from config.const import AutoWaightConst


class AutoWaitPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = AutoWaitLocators(self.page)
        self.const = AutoWaightConst()
        self.timeout = 11000

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        bullet3 = self.locators.bullet_locators(3)
        bullet4 = self.locators.bullet_locators(4)
        bullet5 = self.locators.bullet_locators(5)
        h4_2 = self.locators.h4_title_locator(2)
        h4_3 = self.locators.h4_title_locator(3)
        btn1 = self.locators.apply_btn_locators(1)
        btn2 = self.locators.apply_btn_locators(2)
        btn3 = self.locators.apply_btn_locators(3)

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.text)
        await expect(h4_1).to_have_text(self.const.h4_title1)
        await expect(bullet1).to_have_text(self.const.bullet1)
        await expect(bullet2).to_have_text(self.const.bullet2)
        await expect(bullet3).to_have_text(self.const.bullet3)
        await expect(bullet4).to_have_text(self.const.bullet4)
        await expect(bullet5).to_have_text(self.const.bullet5)
        await expect(h4_2).to_have_text(self.const.h4_title2)
        await expect(h4_3).to_have_text(self.const.h4_title3)
        await expect(btn1).to_have_text(self.const.btn3)
        await expect(btn2).to_have_text(self.const.btn5)
        await expect(btn3).to_have_text(self.const.btn10)

    async def change_target_element(
            self,
            data: str,
    ) -> None | False:
        """Select target element

        Args:
            data (str): Input / Button / Textarea / Select / Label

        Returns:
            None | False: False, if such option is not exist
        """
        locator = self.locators.state_select_locator
        data = data.strip().title()
        if data in self.const.target_element_list:
            await locator.select_option(data)
        else:
            return False

    async def check_status_text(
            self,
            data: str,
    ) -> bool:
        """Checks status text

        Args:
            data (str): default / clicked / restored / wait (3 / 5 / 10)

        Returns:
            bool: True, if status text is as expected
        """
        data = data.lower().strip()
        locator = self.locators.status_text_locator

        if data == 'default':
            text = self.const.status_text_none
        elif data == 'none':
            text = ''
        elif data == 'clicked':
            text = self.const.status_text_clicked
        elif data == 'restored':
            text = self.const.status_text_restored
        elif data == 'wait 3':
            text = self.const.status_text_wait_format.format(3)
        elif data == 'wait 5':
            text = self.const.status_text_wait_format.format(5)
        elif data == 'wait 10':
            text = self.const.status_text_wait_format.format(10)
        else:
            text = ''

        await expect(locator).to_have_text(text)

    async def change_target(
            self,
            data: str,
    ) -> None:
        """Change targets attributes

        Args:
            data (str): visible / enabled / editable / on top / non zero size
        """
        data = data.lower().strip()

        if data == 'visible':
            option = self.const.visibility
        elif data == 'enabled':
            option = self.const.enabled
        elif data == 'editable':
            option = self.const.editable
        elif data == 'on top':
            option = self.const.top
        elif data == 'non zero size':
            option = self.const.non_zero
        else:
            option = ''

        locator = self.locators.check_boxes_locators(option)
        await locator.click()

    async def click_apply(
            self,
            data: int,
    ) -> None | False:
        """Click on Apply button with exact timer

        Args:
            data (int): 3 / 5 / 10

        Returns:
            None | False: Clikc on Apply buton with timer. Return F
        """
        if data == 3:
            locator = self.locators.apply_btn_locators(1)
        elif data == 5:
            locator = self.locators.apply_btn_locators(2)
        elif data == 10:
            locator = self.locators.apply_btn_locators(3)
        else:
            return False

        await locator.click()

    async def click_on_target(self) -> None:
        locator = self.locators.target_locator
        await locator.click(timeout=self.timeout)

    async def fill_target(
            self,
            data: str,
    ) -> None:
        locator = self.locators.target_locator
        await locator.click(force=True, timeout=self.timeout)
        await locator.fill(data, timeout=self.timeout)

    async def check_target_data(
            self,
            data: str,
    ) -> bool:
        locator = self.locators.target_locator
        await expect(locator).to_have_value(data)

    async def check_targets_text(self) -> bool:
        locator = self.locators.target_locator
        await expect(locator).to_have_text(self.const.target_label)

    async def select_target_option(
            self,
            data: int,
    ) -> None | False:
        """Selects item option

        Args:
            data (int): 1 / 2 / 3

        Returns:
            None | False: Select item. False, if data is not correct
        """
        locator = self.locators.target_locator

        if data not in [1, 2, 3]:
            return False

        await locator.select_option(
            self.const.target_options_format.format(data),
            timeout=self.timeout)

    async def check_targets_visibility(self) -> bool:
        """Checks is target is not visible

        Returns:
            bool: True, if target is not visible
        """
        locator = self.locators.target_locator
        await expect(locator).not_to_be_visible()

    async def check_is_targets_hidden(self) -> bool:
        """Checks is target is hidden

        Returns:
            bool: True, if target is hidden
        """
        locator = self.locators.target_locator
        await expect(locator).to_be_hidden()

    async def check_is_target_disabled(self) -> bool:
        locator = self.locators.target_locator
        await expect(locator).to_be_disabled()

    async def check_is_target_editable(self) -> bool:
        locator = self.locators.target_locator
        await expect(locator).to_be_editable()

    async def check_target_is_not_clickable(self) -> bool:
        locator = self.locators.target_locator
        try:
            await locator.click(timeout=2000)
        except playwright.async_api.TimeoutError:
            return True
        else:
            return False
