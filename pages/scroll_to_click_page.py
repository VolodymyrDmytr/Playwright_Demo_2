from playwright.async_api import Page, expect

from pages.base_page import BasePage
from config.locators import ScrollToClickLocators
from config.const import ScrollToClickConst


class ScrollToClickPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ScrollToClickLocators(self.page)
        self.const = ScrollToClickConst()

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locators(1)
        h4_title1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        bullet3 = self.locators.bullet_locators(3)
        bullet4 = self.locators.bullet_locators(4)
        bullet5 = self.locators.bullet_locators(5)
        h4_title2 = self.locators.h4_title_locator(2)
        h5_1 = self.locators.h5_locators(1)
        h5_2 = self.locators.h5_locators(2)
        h5_3 = self.locators.h5_locators(3)
        h5_4 = self.locators.h5_locators(4)
        h5_1_text = self.locators.text_locators(2)
        h5_2_text = self.locators.text_locators(3)
        h5_3_text = self.locators.text_locators(4)
        h5_4_text = self.locators.text_locators(6)
        btns = [self.locators.btn1_locator,
                self.locators.btn2_locator,
                self.locators.btn3_locator,
                self.locators.btn4_locator]

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.text)
        await expect(h4_title1).to_have_text(self.const.h4_title1)
        await expect(bullet1).to_have_text(self.const.bullet1)
        await expect(bullet2).to_have_text(self.const.bullet2)
        await expect(bullet3).to_have_text(self.const.bullet3)
        await expect(bullet4).to_have_text(self.const.bullet4)
        await expect(bullet5).to_have_text(self.const.bullet5)
        await expect(h4_title2).to_have_text(self.const.h4_title2)
        await expect(h5_1).to_have_text(self.const.h5_1)
        await expect(h5_1_text).to_have_text(self.const.h5_1_text)
        await expect(h5_2).to_have_text(self.const.h5_2)
        await expect(h5_2_text).to_have_text(self.const.h5_2_text)
        await expect(h5_3).to_have_text(self.const.h5_3)
        await expect(h5_3_text).to_have_text(self.const.h5_3_text)
        await expect(h5_4).to_have_text(self.const.h5_4)
        await expect(h5_4_text).to_have_text(self.const.h5_4_text)

        for i in range(1, len(btns)+1):
            if i == 4:
                text = self.const.btn4
            else:
                text = self.const.btn_format.format(i)

            await expect(btns[i - 1]).to_have_text(text)

    async def check_status_text(
            self,
            data: int,
    ) -> bool:
        if data == 4:
            text = self.const.status_text_done
        else:
            text = self.const.status_text_format.format(data)

        locator = self.locators.status_text_locator

        await expect(locator).to_have_text(text)

    async def click_on_btn1(self) -> None:
        locator = self.locators.btn1_locator
        await locator.click()

    async def click_on_btn2(self) -> None:
        locator = self.locators.btn2_locator
        await locator.click()

    async def click_on_btn3(self) -> None:
        locator = self.locators.btn3_locator
        await locator.click()

    async def click_on_btn4(self) -> None:
        list_locator = self.locators.list_locators(3)
        btn_locator = self.locators.btn4_locator

        await list_locator.hover()
        await btn_locator.click()
