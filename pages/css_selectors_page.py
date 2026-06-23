from playwright.async_api import Page, expect, Locator
import playwright.async_api

from pages.base_page import BasePage
from config.locators import CSSSelectorsLocators
from config.const import CSSSelectorsConst


class CSSSelectorsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = CSSSelectorsLocators(self.page)
        self.const = CSSSelectorsConst()

    async def _try_to_click(
            self,
            data: Locator,
    ) -> bool:
        try:
            await data.click(timeout=2000)
        except playwright.async_api.TimeoutError:
            return True
        else:
            return False

    async def check_main_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        bullet3 = self.locators.bullet_locators(3)
        h4_2 = self.locators.h4_title_locator(2)

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.text)
        await expect(h4_1).to_have_text(self.const.h4_title1)
        await expect(bullet1).to_have_text(self.const.bullet1)
        await expect(bullet2).to_have_text(self.const.bullet2)
        await expect(bullet3).to_have_text(self.const.bullet3)
        await expect(h4_2).to_have_text(self.const.h4_title2)

    # 1
    async def check_b1_content(self) -> bool:
        h5 = self.locators.h5_locators(1)
        btn = self.locators.b1_btn_locator

        await expect(h5).to_have_text(self.const.h5_1)
        await expect(btn).to_have_text(self.const.h5_1_btn)

    async def b1_click_on_btn(self) -> None:
        locator = self.locators.b1_btn_locator
        await locator.click()

    # 2
    async def check_b2_content(self) -> bool:
        h5 = self.locators.h5_locators(2)
        btn1 = self.locators.b2_btn1_locator
        btn2 = self.locators.b2_btn2_locator
        btn3 = self.locators.b2_btn3_locator

        await expect(h5).to_have_text(self.const.h5_2)
        await expect(btn1).to_have_text(self.const.h5_2_btn1)
        await expect(btn2).to_have_text(self.const.h5_2_btn2)
        await expect(btn3).to_have_text(self.const.h5_2_btn3)

    async def b2_click_on_btn1(self) -> None:
        locator = self.locators.b2_btn1_locator
        await locator.click()

    async def b2_click_on_btn2(self) -> None:
        locator = self.locators.b2_btn2_locator
        await locator.click()

    async def b2_click_on_btn3(self) -> None:
        locator = self.locators.b2_btn3_locator
        await locator.click()

    # 3
    async def check_b3_content(self) -> bool:
        h5 = self.locators.h5_locators(3)
        link = self.locators.b3_link_locator
        chip1 = self.locators.b3_chip_act_locator
        chip2 = self.locators.b3_chip_inact_locator

        await expect(h5).to_have_text(self.const.h5_3)
        await expect(link).to_have_text(self.const.h5_3_link)
        await expect(chip1).to_have_text(self.const.h5_3_chips1)
        await expect(chip2).to_have_text(self.const.h5_3_chips2)

    async def b3_fill_fields(
            self,
            username: str,
            email: str,
    ) -> None:
        name_locator = self.locators.b3_field1_locator
        email_locator = self.locators.b3_field2_locator

        await name_locator.fill(username)
        await email_locator.fill(email)

    async def b3_check_fields_data(
            self,
            username: str,
            email: str,
    ) -> bool:
        name_locator = self.locators.b3_field1_locator
        email_locator = self.locators.b3_field2_locator

        await expect(name_locator).to_have_value(username)
        await expect(email_locator).to_have_value(email)

    async def b3_click_on_link(self) -> None:
        locator = self.locators.b3_link_locator

        with self.page.context.expect_page() as new_page:
            await locator.click()

        new_page = new_page.value

        await expect(new_page).to_have_title(self.const.title)
        await expect(new_page).to_have_url(self.const.link)

    async def b3_check_chip_status(
            self,
            chip: int,
            is_active: bool,
    ) -> bool:
        # Locator
        if chip == 1:
            locator = self.locators.b3_chip_act_locator
        elif chip == 2:
            locator = self.locators.b3_chip_inact_locator
        else:
            return False

        # Check
        if is_active is True:
            await expect(locator).to_have_attribute('data-status', 'active')
        else:
            await expect(locator).to_have_attribute('data-status', 'inactive')

    # 4
    async def check_b4_content(self) -> bool:
        h5 = self.locators.h5_locators(4)
        bullet1 = self.locators.b4_bullet_locators(1)
        bullet2 = self.locators.b4_bullet_locators(2)
        bullet3 = self.locators.b4_bullet_locators(3)
        p1 = self.locators.b4_p1_locator
        p2 = self.locators.b4_p2_locator
        p3 = self.locators.b4_p3_locator

        await expect(h5).to_have_text(self.const.h5_4)
        await expect(bullet1).to_have_text(self.const.h5_4_bullet1)
        await expect(bullet2).to_have_text(self.const.h5_4_bullet2)
        await expect(bullet3).to_have_text(self.const.h5_4_bullet3)
        await expect(p1).to_have_text(self.const.h5_4_p1)
        await expect(p2).to_have_text(self.const.h5_4_p2)
        await expect(p3).to_have_text(self.const.h5_4_p3)

    # 5
    async def check_b5_content(self) -> bool:
        h5 = self.locators.h5_locators(5)

        await expect(h5).to_have_text(self.const.h5_5)

        for row_id in range(0, len(self.const.h5_5_table)):
            current_row = self.const.h5_5_table[row_id]

            for cell_id in range(0, len(current_row)):

                locator = self.locators.b5_table(row_id + 1, cell_id + 1)
                cell_data = current_row[cell_id]

                await expect(locator).to_have_text(cell_data)

    # 6
    async def check_b6_content(self) -> bool:
        h5 = self.locators.h5_locators(6)
        btn1 = self.locators.b6_btn_visible_locator
        btn2 = self.locators.b6_btn_not_displayed_locator
        btn3 = self.locators.b6_btn_not_visible_locator
        btn4 = self.locators.b6_btn_hidden_overflow_locator
        btn5 = self.locators.b6_btn_hidden_locator
        btn6 = self.locators.b6_btn_offscreen_locator

        await expect(h5).to_have_text(self.const.h5_6)
        await expect(btn1).to_have_text(self.const.h5_6_btn1)
        await expect(btn2).to_have_text(self.const.h5_6_btn2)
        await expect(btn3).to_have_text(self.const.h5_6_btn3)
        await expect(btn4).to_have_text(self.const.h5_6_btn4)
        await expect(btn5).to_have_text(self.const.h5_6_btn5)
        await expect(btn6).to_have_text(self.const.h5_6_btn6)

    async def check_is_btn1_visible(self) -> bool:
        locator = self.locators.b6_btn_visible_locator
        await expect(locator).to_be_visible()

    async def check_is_bnt2_not_displayed(self) -> bool:
        locator = self.locators.b6_btn_not_displayed_locator
        await expect(locator).not_to_be_disabled()

    async def check_is_bnt3_not_visible(self) -> bool:
        locator = self.locators.b6_btn_not_visible_locator
        await expect(locator).not_to_be_visible()

    async def check_is_bnt4_not_visible(self) -> bool:
        locator = self.locators.b6_btn_hidden_overflow_locator
        await self._try_to_click(locator)

    async def check_is_bnt5_to_be_hidden(self) -> bool:
        locator = self.locators.b6_btn_hidden_locator
        await expect(locator).to_have_css('opacity', '0')

    async def check_is_bnt6_to_be_offscreen(self) -> bool:
        locator = self.locators.b6_btn_offscreen_locator
        await expect(locator).not_to_be_in_viewport()

    # 7
    async def check_b7_content(self) -> bool:
        h5 = self.locators.h5_locators(7)
        text = self.locators.b7_text_locator
        title1 = self.locators.b7_1_title_locator
        btn1 = self.locators.b7_1_btn_locator
        title2 = self.locators.b7_2_title_locator
        btn2 = self.locators.b7_2_btn_locator
        title3 = self.locators.b7_3_title_locator
        btn3 = self.locators.b7_3_btn_locator

        await expect(h5).to_have_text(self.const.h5_7)
        await expect(text).to_have_text(self.const.h5_7_text)
        await expect(title1).to_have_text(self.const.h5_7_title1)
        await expect(btn1).to_have_text(self.const.h5_7_btn1)
        await expect(title2).to_have_text(self.const.h5_7_title2)
        await expect(btn2).to_have_text(self.const.h5_7_btn2)
        await expect(title3).to_have_text(self.const.h5_7_title3)
        await expect(btn3).to_have_text(self.const.h5_7_btn3)

    async def b7_click_on_btn(
            self,
            data: int,
    ) -> None | False:
        if data == 1:
            locator = self.locators.b7_1_btn_locator
        elif data == 2:
            locator = self.locators.b7_2_btn_locator
        elif data == 3:
            locator = self.locators.b7_3_btn_locator
        else:
            return False

        await locator.click()

    def _b7_field_locators(
            self,
            level: int,
    ) -> Locator:
        if level == 1:
            return self.locators.b7_1_field_locator
        elif level == 2:
            return self.locators.b7_2_field_locator
        elif level == 3:
            return self.locators.b7_3_field_locator
        else:
            return Locator()

    async def b7_fill_field(
            self,
            level: int,
            data: str,
    ) -> None:
        locator = self._b7_field_locators(level)
        await locator.fill(data)

    async def b7_check_field(
            self,
            level: int,
            data: str,
    ) -> bool:
        locator = self._b7_field_locators(level)
        await expect(locator).to_have_value(data)

    async def b7_check_status(self) -> bool:
        locator = self.locators.b7_3_status_locator
        await expect(locator).to_have_text(self.const.h5_7_status)
