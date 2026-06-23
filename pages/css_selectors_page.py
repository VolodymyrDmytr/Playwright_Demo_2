from playwright.sync_api import Page, expect, Locator
import playwright.sync_api

from pages.base_page import BasePage
from config.locators import CSSSelectorsLocators
from config.const import CSSSelectorsConst


class CSSSelectorsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = CSSSelectorsLocators(self.page)
        self.const = CSSSelectorsConst()

    def _try_to_click(
            self,
            data: Locator,
    ) -> bool:
        try:
            data.click(timeout=2000)
        except playwright.sync_api.TimeoutError:
            return True
        else:
            return False

    def check_main_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        bullet3 = self.locators.bullet_locators(3)
        h4_2 = self.locators.h4_title_locator(2)

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(bullet3).to_have_text(self.const.bullet3)
        expect(h4_2).to_have_text(self.const.h4_title2)

    # 1
    def check_b1_content(self) -> bool:
        h5 = self.locators.h5_locators(1)
        btn = self.locators.b1_btn_locator

        expect(h5).to_have_text(self.const.h5_1)
        expect(btn).to_have_text(self.const.h5_1_btn)

    def b1_click_on_btn(self) -> None:
        locator = self.locators.b1_btn_locator
        locator.click()

    # 2
    def check_b2_content(self) -> bool:
        h5 = self.locators.h5_locators(2)
        btn1 = self.locators.b2_btn1_locator
        btn2 = self.locators.b2_btn2_locator
        btn3 = self.locators.b2_btn3_locator

        expect(h5).to_have_text(self.const.h5_2)
        expect(btn1).to_have_text(self.const.h5_2_btn1)
        expect(btn2).to_have_text(self.const.h5_2_btn2)
        expect(btn3).to_have_text(self.const.h5_2_btn3)

    def b2_click_on_btn1(self) -> None:
        locator = self.locators.b2_btn1_locator
        locator.click()

    def b2_click_on_btn2(self) -> None:
        locator = self.locators.b2_btn2_locator
        locator.click()

    def b2_click_on_btn3(self) -> None:
        locator = self.locators.b2_btn3_locator
        locator.click()

    # 3
    def check_b3_content(self) -> bool:
        h5 = self.locators.h5_locators(3)
        link = self.locators.b3_link_locator
        chip1 = self.locators.b3_chip_act_locator
        chip2 = self.locators.b3_chip_inact_locator

        expect(h5).to_have_text(self.const.h5_3)
        expect(link).to_have_text(self.const.h5_3_link)
        expect(chip1).to_have_text(self.const.h5_3_chips1)
        expect(chip2).to_have_text(self.const.h5_3_chips2)

    def b3_fill_fields(
            self,
            username: str,
            email: str,
    ) -> None:
        name_locator = self.locators.b3_field1_locator
        email_locator = self.locators.b3_field2_locator

        name_locator.fill(username)
        email_locator.fill(email)

    def b3_check_fields_data(
            self,
            username: str,
            email: str,
    ) -> bool:
        name_locator = self.locators.b3_field1_locator
        email_locator = self.locators.b3_field2_locator

        expect(name_locator).to_have_value(username)
        expect(email_locator).to_have_value(email)

    def b3_click_on_link(self) -> None:
        locator = self.locators.b3_link_locator

        with self.page.context.expect_page() as new_page:
            locator.click()

        new_page = new_page.value

        expect(new_page).to_have_title(self.const.title)
        expect(new_page).to_have_url(self.const.link)

    def b3_check_chip_status(
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
            expect(locator).to_have_attribute('data-status', 'active')
        else:
            expect(locator).to_have_attribute('data-status', 'inactive')

    # 4
    def check_b4_content(self) -> bool:
        h5 = self.locators.h5_locators(4)
        bullet1 = self.locators.b4_bullet_locators(1)
        bullet2 = self.locators.b4_bullet_locators(2)
        bullet3 = self.locators.b4_bullet_locators(3)
        p1 = self.locators.b4_p1_locator
        p2 = self.locators.b4_p2_locator
        p3 = self.locators.b4_p3_locator

        expect(h5).to_have_text(self.const.h5_4)
        expect(bullet1).to_have_text(self.const.h5_4_bullet1)
        expect(bullet2).to_have_text(self.const.h5_4_bullet2)
        expect(bullet3).to_have_text(self.const.h5_4_bullet3)
        expect(p1).to_have_text(self.const.h5_4_p1)
        expect(p2).to_have_text(self.const.h5_4_p2)
        expect(p3).to_have_text(self.const.h5_4_p3)

    # 5
    def check_b5_content(self) -> bool:
        h5 = self.locators.h5_locators(5)

        expect(h5).to_have_text(self.const.h5_5)

        for row_id in range(0, len(self.const.h5_5_table)):
            current_row = self.const.h5_5_table[row_id]

            for cell_id in range(0, len(current_row)):

                locator = self.locators.b5_table(row_id + 1, cell_id + 1)
                cell_data = current_row[cell_id]

                expect(locator).to_have_text(cell_data)

    # 6
    def check_b6_content(self) -> bool:
        h5 = self.locators.h5_locators(6)
        btn1 = self.locators.b6_btn_visible_locator
        btn2 = self.locators.b6_btn_not_displayed_locator
        btn3 = self.locators.b6_btn_not_visible_locator
        btn4 = self.locators.b6_btn_hidden_overflow_locator
        btn5 = self.locators.b6_btn_hidden_locator
        btn6 = self.locators.b6_btn_offscreen_locator

        expect(h5).to_have_text(self.const.h5_6)
        expect(btn1).to_have_text(self.const.h5_6_btn1)
        expect(btn2).to_have_text(self.const.h5_6_btn2)
        expect(btn3).to_have_text(self.const.h5_6_btn3)
        expect(btn4).to_have_text(self.const.h5_6_btn4)
        expect(btn5).to_have_text(self.const.h5_6_btn5)
        expect(btn6).to_have_text(self.const.h5_6_btn6)

    def check_is_btn1_visible(self) -> bool:
        locator = self.locators.b6_btn_visible_locator
        expect(locator).to_be_visible()

    def check_is_bnt2_not_displayed(self) -> bool:
        locator = self.locators.b6_btn_not_displayed_locator
        expect(locator).not_to_be_disabled()

    def check_is_bnt3_not_visible(self) -> bool:
        locator = self.locators.b6_btn_not_visible_locator
        expect(locator).not_to_be_visible()

    def check_is_bnt4_not_visible(self) -> bool:
        locator = self.locators.b6_btn_hidden_overflow_locator
        self._try_to_click(locator)

    def check_is_bnt5_to_be_hidden(self) -> bool:
        locator = self.locators.b6_btn_hidden_locator
        expect(locator).to_have_css('opacity', '0')

    def check_is_bnt6_to_be_offscreen(self) -> bool:
        locator = self.locators.b6_btn_offscreen_locator
        expect(locator).not_to_be_in_viewport()

    # 7
    def check_b7_content(self) -> bool:
        h5 = self.locators.h5_locators(7)
        text = self.locators.b7_text_locator
        title1 = self.locators.b7_1_title_locator
        btn1 = self.locators.b7_1_btn_locator
        title2 = self.locators.b7_2_title_locator
        btn2 = self.locators.b7_2_btn_locator
        title3 = self.locators.b7_3_title_locator
        btn3 = self.locators.b7_3_btn_locator

        expect(h5).to_have_text(self.const.h5_7)
        expect(text).to_have_text(self.const.h5_7_text)
        expect(title1).to_have_text(self.const.h5_7_title1)
        expect(btn1).to_have_text(self.const.h5_7_btn1)
        expect(title2).to_have_text(self.const.h5_7_title2)
        expect(btn2).to_have_text(self.const.h5_7_btn2)
        expect(title3).to_have_text(self.const.h5_7_title3)
        expect(btn3).to_have_text(self.const.h5_7_btn3)

    def b7_click_on_btn(
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

        locator.click()

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

    def b7_fill_field(
            self,
            level: int,
            data: str,
    ) -> None:
        locator = self._b7_field_locators(level)
        locator.fill(data)

    def b7_check_field(
            self,
            level: int,
            data: str,
    ) -> bool:
        locator = self._b7_field_locators(level)
        expect(locator).to_have_value(data)

    def b7_check_status(self) -> bool:
        locator = self.locators.b7_3_status_locator
        expect(locator).to_have_text(self.const.h5_7_status)
