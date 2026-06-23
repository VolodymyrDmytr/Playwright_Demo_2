from playwright.async_api import Page, expect
from pathlib import Path

from pages.base_page import BasePage
from config.locators import FileUploadLocators
from config.const import FileUploadConst


class FileUploadPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = FileUploadLocators(self.page)
        self.const = FileUploadConst()

    async def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        upload_title = self.locators.upload_title_locator
        upload_text = self.locators.upload_text_locator
        upload_btn = self.locators.upload_btn_locator

        await expect(h3).to_have_text(self.const.h3)
        await expect(text).to_have_text(self.const.text)
        await expect(h4_1).to_have_text(self.const.h4_title1)
        await expect(bullet1).to_have_text(self.const.bullet1)
        await expect(bullet2).to_have_text(self.const.bullet2)
        await expect(h4_2).to_have_text(self.const.h4_title2)
        await expect(upload_title).to_have_text(self.const.upload_title)
        await expect(upload_text).to_have_text(self.const.upload_text)
        await expect(upload_btn).to_have_text(self.const.btn_text)

    async def upload_test_file(
            self,
            data: str = FileUploadConst.file_name,
    ) -> None:
        path = Path(__file__).parent.parent / f'test_files/{data}'
        locator = self.locators.upload_btn_locator

        await locator.set_input_files(path)

    async def remove_file(
            self,
            data: int,
    ) -> None:
        locator = self.locators.remove_file_btn_locators(data)
        await locator.click()

    async def check_amount_of_uploaded_files(
            self,
            data: int,
    ) -> bool:
        locator = self.locators.upload_amount_locator
        txt = self.const.amount_format.format(data)

        await expect(locator).to_have_text(txt)

    async def amount_of_uploaded_files_is_not_shown(self) -> bool:
        text = self.const.amount_format.format(1)
        locator = self.locators.upload_amount_locator

        await expect(locator).not_to_have_text(text)

    async def check_file_name(
            self,
            number: int,
            file_name: str,
    ) -> bool:
        locator = self.locators.file_name_locators(number)
        await expect(locator).to_have_text(file_name)
