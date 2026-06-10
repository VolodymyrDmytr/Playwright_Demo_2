from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from config.const import ClassAttributeConst
from config.locators import ClassAttributeLocators


class ClassAttributePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ClassAttributeLocators(self.page)
        self.const = ClassAttributeConst()

    def check_page_text(self) -> bool:
        h3 = self.locators.h3_title_locator
        txt1 = self.locators.text_locator(1)
        html = self.locators.html_code_locator
        txt2 = self.locators.text_locator(2)
        bash1 = self.locators.bash_code_locator(1)
        txt3 = self.locators.text_locator(3)
        bash2 = self.locators.bash_code_locator(2)
        h4_title1 = self.locators.h4_title1_locator
        bullet1 = self.locators.bullet_locator(1)
        bullet2 = self.locators.bullet_locator(2)
        h4_title2 = self.locators.h4_title2_locator
        btns = [self.locators.green_btn_locator,
                self.locators.blue_btn_locator,
                self.locators.orange_btn_locator]

        expect(h3).to_have_text(self.const.h3_title)
        expect(txt1).to_have_text(self.const.text1)
        expect(html).to_have_text(self.const.html)
        expect(txt2).to_have_text(self.const.text2)
        expect(bash1).to_have_text(self.const.bash1)
        expect(txt3).to_have_text(self.const.text3)
        expect(bash2).to_have_text(self.const.bash2)
        expect(h4_title1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(h4_title2).to_have_text(self.const.h4_title2)
        for element in btns:
            expect(element).to_have_text(self.const.btn_text)

    def click_btn(
            self,
            data: str,
    ) -> None:
        """Clicks on button

        Args:
            data (str): green / blue / orange
        """
        data = data.lower()

        if data == 'green':
            self.locators.green_btn_locator.click()
        elif data == 'blue':
            self.locators.blue_btn_locator.click()
        elif data == 'orange':
            self.locators.orange_btn_locator.click()

    def _handle_dialog(self, dialog):
        assert dialog.message == self.const.alert_text
        dialog.accept()

    def accept_and_check_alert_text(self) -> bool:
        self.page.on('dialog', self._handle_dialog)

    def accept_alert(self) -> bool:
        self.page.on('dialog', lambda d: d.accept())
