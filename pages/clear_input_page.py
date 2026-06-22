from playwright.sync_api import Page, expect, Locator

from pages.base_page import BasePage
from config.locators import ClearInputLocators
from config.const import ClearInputConst


class ClearInputPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ClearInputLocators(self.page)
        self.const = ClearInputConst()

    def _field_locator_by_number(
            self,
            data: int,
    ) -> Locator:
        if data == 1:
            return self.locators.input_locator
        elif data == 2:
            return self.locators.textarea_locator
        elif data == 3:
            return self.locators.input_password_locator
        elif data == 4:
            return self.locators.input_email_locator
        elif data == 5:
            return self.locators.input_number_locator
        elif data == 6:
            return self.locators.input_search_locator
        elif data == 7:
            return self.locators.input_url_locator
        elif data == 8:
            return self.locators.input_phone_locator
        elif data == 9:
            return self.locators.input_div_locator
        else:
            return Locator()

    def fields_amount(self) -> int:
        return self.locators.label_locators.count()

    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        bullet3 = self.locators.bullet_locators(3)
        bullet4 = self.locators.bullet_locators(4)
        h4_2 = self.locators.h4_title_locator(2)
        label1 = self.locators.label_locator(1)
        label2 = self.locators.label_locator(2)
        label3 = self.locators.label_locator(3)
        label4 = self.locators.label_locator(4)
        label5 = self.locators.label_locator(5)
        label6 = self.locators.label_locator(6)
        label7 = self.locators.label_locator(7)
        label8 = self.locators.label_locator(8)
        label9 = self.locators.label_locator(9)
        field1 = self._field_locator_by_number(1)
        field2 = self._field_locator_by_number(2)
        field3 = self._field_locator_by_number(3)
        field4 = self._field_locator_by_number(4)
        field5 = self._field_locator_by_number(5)
        field6 = self._field_locator_by_number(6)
        field7 = self._field_locator_by_number(7)
        field8 = self._field_locator_by_number(8)
        field9 = self._field_locator_by_number(9)

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(bullet3).to_have_text(self.const.bullet3)
        expect(bullet4).to_have_text(self.const.bullet4)
        expect(h4_2).to_have_text(self.const.h4_title2)
        expect(label1).to_have_text(self.const.label1)
        expect(label2).to_have_text(self.const.label2)
        expect(label3).to_have_text(self.const.label3)
        expect(label4).to_have_text(self.const.label4)
        expect(label5).to_have_text(self.const.label5)
        expect(label6).to_have_text(self.const.label6)
        expect(label7).to_have_text(self.const.label7)
        expect(label8).to_have_text(self.const.label8)
        expect(label9).to_have_text(self.const.label9)
        expect(field1).to_have_value(self.const.value1)
        expect(field2).to_have_value(self.const.value2)
        assert len(field3.input_value()) == self.const.value3_char
        expect(field4).to_have_value(self.const.value4)
        expect(field5).to_have_value(self.const.value5)
        expect(field6).to_have_value(self.const.value6)
        expect(field7).to_have_value(self.const.value7)
        expect(field8).to_have_value(self.const.value8)
        expect(field9).to_have_text(self.const.value9)

    def check_status_text(
            self,
            data: int,
    ) -> bool:
        if data == 0:
            text = self.const.status_text_done
        else:
            text = self.const.status_text_form.format(data)

        locator = self.locators.status_text_locator

        expect(locator).to_have_text(text)

    def remove_data(
            self,
            data: int,
    ) -> None:
        locator = self._field_locator_by_number(data)

        locator.fill('')

    def fill_data(
            self,
            field: int,
            data: str | int,
    ) -> None:
        locator = self._field_locator_by_number(field)

        locator.fill(data)

    def check_field_is_empty(
            self,
            data: int,
    ) -> bool:
        locator = self._field_locator_by_number(data)

        expect(locator).to_have_text('')
