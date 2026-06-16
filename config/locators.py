from playwright.sync_api import Page, Locator


class BaseLocators:

    def __init__(self, page: Page):
        self.page = page

    def link_locator(
            self,
            data: str,
    ) -> Locator:
        """Links locator by its text

        Args:
            data (str): link text

        Returns:
            Locator: Links locator
        """
        return self.page.get_by_role('link', name=data, exact=True)


class PageLocators(BaseLocators):

    def __init__(self, page: Page):
        self.page = page

    @property
    def h3_locator(self) -> Locator:
        return self.page.locator('//h3')

    @property
    def _text_locator(self) -> Locator:
        return self.page.locator('//p')

    @property
    def text_locator(self) -> Locator:
        return self._text_locator.first

    def h4_title_locator(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('//h4').nth(data)

    def bullet_locators(
            self,
            data: int,
    ) -> Locator:
        data += 1
        return self.page.locator('//li').nth(data)


class HomePageLocators(BaseLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def title_locator(self) -> Locator:
        return self.page.locator('//h1')

    @property
    def quotes_locator(self) -> Locator:
        return self.page.locator('.mb-0')

    @property
    def author_locator(self) -> Locator:
        return self.page.locator('.blockquote-footer')

    @property
    def purpose_locator(self) -> Locator:
        return self.page.locator('.alert-warning')

    @property
    def text_locator(self) -> Locator:
        return self.page.locator('//*[@id="description"]//p').nth(1)

    @property
    def cards_locator(self) -> Locator:
        return self.page.locator('.col-sm')

    def card_title_locator(
            self,
            number: int,
    ) -> Locator:
        card_locator = self.cards_locator.nth(number)
        return card_locator.locator('//h3')

    def card_description_locator(
            self,
            number: int,
    ) -> Locator:
        card_locator = self.cards_locator.nth(number)
        return card_locator.locator('//p')

    @property
    def img_locator(self) -> Locator:
        return self.page.locator('.img-fluid')

    @property
    def img_text_locator(self) -> Locator:
        return self.page.locator('.text-center')


class DynamicIdLoators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def button_locator(self) -> Locator:
        return self.page.locator('.btn-primary')


class ClassAttributeLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def green_btn_locator(self) -> Locator:
        return self.page.locator('.btn-success')

    @property
    def blue_btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')

    @property
    def orange_btn_locator(self) -> Locator:
        return self.page.locator('.btn-warning')

    def text_locator(
            self,
            data: int,
    ) -> Locator | bool:
        data -= 1
        return self.page.locator('//p').nth(data)

    @property
    def html_code_locator(self) -> Locator:
        return self.page.locator('.language-html').first

    def bash_code_locator(
            self,
            data: int,
    ) -> Locator | bool:
        data -= 1
        return self.page.locator(
            "//code[contains(@class, 'language-bash')]").nth(data)


class HiddenLayersLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def btn_locator(self) -> Locator:
        return self.page.locator('.btn-success')

    @property
    def success_locator(self) -> Locator:
        return self.page.locator('.spa-view').nth(1)


class LoadDelaysLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')


class AjaxDataLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')

    @property
    def success_txt_locator(self) -> Locator:
        return self.page.locator('.bg-success')


class ClientSideDelayLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')

    @property
    def success_txt_locator(self) -> Locator:
        return self.page.locator('.bg-success')


class ClickLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')

    @property
    def success_btn_locator(self) -> Locator:
        return self.page.locator('.btn-success')


class TextInputLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')

    @property
    def field_name_locator(self) -> Locator:
        return self.page.locator('//label')

    @property
    def field_locator(self) -> Locator:
        return self.page.locator('.form-control')


class ScrollbarsLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')


class DynamicTableLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def table_name_locator(self) -> Locator:
        return self.page.locator("//div[@id='table_desc']")

    @property
    def expected_result_locator(self) -> Locator:
        return self.page.locator('.bg-warning')

    @property
    def table_row_locators(
        self,
    ) -> Locator:
        return self.page.get_by_role('row')

    def table_cell_in_row_locators(
            self,
            row: int,
    ) -> Locator:
        row_locator = self.table_row_locators.nth(row)
        return row_locator.get_by_role('cell')

    @property
    def header_cell_locators(self) -> Locator:
        return self.page.locator("//span[@role='columnheader']")


class VerifyTextLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    def text_locators(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self._text_locator.nth(data)

    def find_text(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('.badge-secondary').nth(data)

    def table_locators(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('.col-sm').nth(data)

    def find_by_text(
            self,
            data: str,
    ) -> Locator:
        return self.page.locator(
            f"//span[normalize-space(.)='{data}']")


class ProgressBarLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def start_btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')

    @property
    def stop_btn_locator(self) -> Locator:
        return self.page.locator('.btn-info')

    @property
    def progress_bar_locator(self) -> Locator:
        return self.page.locator('.progress-bar')

    @property
    def result_locator(self) -> Locator:
        return self.page.locator("//p[@id='result']")


class VisibilityLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def blue_btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')

    @property
    def red_btn_locator(self) -> Locator:
        return self.page.locator('.btn-danger')

    @property
    def yellow_btn_locator(self) -> Locator:
        return self.page.locator('.btn-warning')

    @property
    def green_btn_locator(self) -> Locator:
        return self.page.locator('.btn-success')

    def info_btns_locator(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('.btn-info').nth(data)


class SampleAppLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def info_text_locator(self) -> Locator:
        return self.page.locator('//label')

    @property
    def name_field_locator(self) -> Locator:
        return self.page.locator('.form-control').nth(0)

    @property
    def passwrd_locator(self) -> Locator:
        return self.page.locator('.form-control').nth(1)

    @property
    def btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')


class MouseOverLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    def text_locators(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self._text_locator.nth(data)

    def link_page_locator(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('.text-primary').nth(data)

    @property
    def link_on_hover_locator(
            self,
    ) -> Locator:
        return self.page.locator('.text-warning')


class NonBreakingSpaceLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def locator_locator(self) -> Locator:
        return self.page.locator('//pre')

    @property
    def button_locator(self) -> Locator:
        return self.page.locator("//button[text()='My\u00A0Button']")


class OverlappedElementLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    def fields_locator(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('//input').nth(data)


class ShadowDOMLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def h6_locator(self) -> Locator:
        return self.page.locator('//h6')

    @property
    def field_locator(self) -> Locator:
        return self.page.locator('.edit-field')

    @property
    def generate_btn_locator(self) -> Locator:
        return self.page.locator('.button-generate')

    @property
    def copy_btn_locator(self) -> Locator:
        return self.page.locator('.button-copy')


class AlertsLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def alert_btn_locator(self) -> Locator:
        return self.page.locator("//button[@id='alertButton']")

    @property
    def confirm_btn_locator(self) -> Locator:
        return self.page.locator("//button[@id='confirmButton']")

    @property
    def prompt_btn_locator(self) -> Locator:
        return self.page.locator("//button[@id='promptButton']")


class FileUploadLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    def remove_file_btn_locators(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self._iframe_locator.locator('.file-actions').nth(data)

    @property
    def _iframe_locator(self) -> Locator:
        return self.page.frame_locator('iframe')

    @property
    def _upload_blocks_text_locator(self) -> Locator:
        return self._iframe_locator.locator('.upload-box').locator('//p')

    @property
    def upload_title_locator(self) -> Locator:
        return self._upload_blocks_text_locator.nth(0)

    @property
    def upload_text_locator(self) -> Locator:
        return self._upload_blocks_text_locator.nth(1)

    def file_name_locators(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        locator = self._iframe_locator.locator('.file-info')
        return locator.locator('//p').nth(data)

    @property
    def upload_amount_locator(self) -> Locator:
        return self._upload_blocks_text_locator.last

    @property
    def upload_btn_locator(self) -> Locator:
        return self._iframe_locator.locator('.browse-btn')


class AnimatedButtonLocator(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def status_text_locator(self) -> Locator:
        return self.page.locator('//div[@id="opstatus"]')

    @property
    def start_btn_locator(self) -> Locator:
        return self.page.locator('.btn-secondary')

    @property
    def target_btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')


class DisabledInputLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def status_text_locator(self) -> Locator:
        return self.page.locator('//div[@id="opstatus"]')

    @property
    def btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')

    @property
    def field_locator(self) -> Locator:
        return self.page.locator('.form-control')
