from playwright.sync_api import Page, Locator

from config.const import CSSSelectorsConst


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


class AutoWaitLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    def apply_btn_locators(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('.btn-secondary').nth(data)

    @property
    def target_locator(self) -> Locator:
        return self.page.locator("//*[@id='target']")

    @property
    def status_text_locator(self) -> Locator:
        return self.page.locator("//div[@id='opstatus']")

    @property
    def state_select_locator(self) -> Locator:
        return self.page.locator('.form-select').first

    def check_boxes_locators(
            self,
            data: str,
    ) -> Locator:
        return self.page.get_by_role('checkbox', name=data)


class FramesLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    #   objects in 1st iframe
    @property
    def iframe1_locator(self) -> Locator:
        return self.page.frame_locator('iframe')

    @property
    def edit_btn_1_locator(self) -> Locator:
        return self.iframe1_locator.locator("//button[@data-action='edit']")

    @property
    def submit_btn_1_locator(self) -> Locator:
        return self.iframe1_locator.get_by_text('Submit')

    @property
    def click_btn_1_locator(self) -> Locator:
        return self.iframe1_locator.locator("//button[@name='my-button']")

    @property
    def primary_btn_1_locator(self) -> Locator:
        return self.iframe1_locator.locator('.btn-class')

    @property
    def status_text_1_locator(self) -> Locator:
        return self.iframe1_locator.locator("//div[@id='result']")

    #   objects in 2nd iframe
    @property
    def iframe2_locator(self) -> Locator:
        return self.iframe1_locator.frame_locator('iframe')

    @property
    def edit_btn_2_locator(self) -> Locator:
        return self.iframe2_locator.locator("//button[@data-action='edit']")

    @property
    def submit_btn_2_locator(self) -> Locator:
        return self.iframe2_locator.get_by_text('Submit')

    @property
    def click_btn_2_locator(self) -> Locator:
        return self.iframe2_locator.locator("//button[@name='my-button']")

    @property
    def primary_btn_2_locator(self) -> Locator:
        return self.iframe2_locator.locator('.btn-class')

    @property
    def status_text_2_locator(self) -> Locator:
        return self.iframe2_locator.locator("//div[@id='result']")


class ClearInputLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def status_text_locator(self) -> Locator:
        return self.page.locator("//div[@id='opstatus']")

    @property
    def label_locators(self) -> Locator:
        return self.page.locator('//label')

    def label_locator(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.label_locators.nth(data)

    @property
    def input_locator(self) -> Locator:
        return self.page.locator("//input[@id='clearInput']")

    @property
    def textarea_locator(self) -> Locator:
        return self.page.locator("//textarea[@id='clearTextarea']")

    @property
    def input_password_locator(self) -> Locator:
        return self.page.locator("//input[@id='clearPassword']")

    @property
    def input_email_locator(self) -> Locator:
        return self.page.locator("//input[@id='clearEmail']")

    @property
    def input_number_locator(self) -> Locator:
        return self.page.locator("//input[@id='clearNumber']")

    @property
    def input_search_locator(self) -> Locator:
        return self.page.locator("//input[@id='clearSearch']")

    @property
    def input_url_locator(self) -> Locator:
        return self.page.locator("//input[@id='clearUrl']")

    @property
    def input_phone_locator(self) -> Locator:
        return self.page.locator("//input[@id='clearTel']")

    @property
    def input_div_locator(self) -> Locator:
        return self.page.locator("//div[@id='clearContentEditable']")


class ScrollToClickLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    def text_locators(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self._text_locator.nth(data)

    def h5_locators(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('//h5').nth(data)

    @property
    def status_text_locator(self) -> Locator:
        return self.page.locator("//span[@id='progressText']")

    def list_locators(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('.hover-row').nth(data)

    @property
    def btn1_locator(self) -> Locator:
        return self.page.locator("//button[@id='scrollTarget1']")

    @property
    def btn2_locator(self) -> Locator:
        return self.page.locator("//button[@id='scrollTarget2']")

    @property
    def btn3_locator(self) -> Locator:
        return self.page.locator("//button[@id='scrollTarget3']")

    @property
    def btn4_locator(self) -> Locator:
        return self.page.locator("//button[@id='scrollTarget4']")


class CSSSelectorsLocators(PageLocators):

    def __init__(self, page: Page):
        super().__init__(page)
        self.const = CSSSelectorsConst()

    def h5_locators(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('//h5').nth(data)

    # 1
    @property
    def b1_btn_locator(self) -> Locator:
        return self.page.locator("//button[@id='primary-btn']")

    # 2
    @property
    def b2_btn1_locator(self) -> Locator:
        return self.page.locator("//button[@data-id='class-btn-first']")

    @property
    def b2_btn2_locator(self) -> Locator:
        return self.page.locator("//button[@data-id='class-btn-second']")

    @property
    def b2_btn3_locator(self) -> Locator:
        return self.page.locator("//button[@data-id='class-btn-third']")

    # 3
    @property
    def b3_field1_locator(self) -> Locator:
        return self.page.get_by_placeholder(self.const.h5_3_field1_placeholder)

    @property
    def b3_field2_locator(self) -> Locator:
        return self.page.get_by_placeholder(self.const.h5_3_field2_placeholder)

    @property
    def b3_link_locator(self) -> Locator:
        return self.link_locator(self.const.h5_3_link)

    @property
    def b3_chip_act_locator(self) -> Locator:
        return self.page.locator('.badge-success')

    @property
    def b3_chip_inact_locator(self) -> Locator:
        return self.page.locator('.badge-secondary')

    # 4
    def b4_bullet_locators(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('.combo-item').nth(data)

    @property
    def b4_p1_locator(self) -> Locator:
        return self.page.locator('.first-para')

    @property
    def b4_p2_locator(self) -> Locator:
        return self.page.locator('.second-para')

    @property
    def b4_p3_locator(self) -> Locator:
        return self.page.locator('.following-span')

    # 5
    def b5_table(
            self,
            row: int,
            cell: int,
    ) -> Locator:
        row -= 1
        cell -= 1

        row_locator = self.page.locator('//tr').nth(row)

        return row_locator.locator('//td').nth(cell)

    # 6
    @property
    def b6_btn_visible_locator(self) -> Locator:
        return self.page.locator('.btn-success')

    @property
    def b6_btn_not_displayed_locator(self) -> Locator:
        return self.page.locator("//button[@id='hidden-display']")

    @property
    def b6_btn_not_visible_locator(self) -> Locator:
        return self.page.locator("//button[@id='hidden-visibility']")

    @property
    def b6_btn_hidden_overflow_locator(self) -> Locator:
        return self.page.locator("//button[@id='hidden-overflow']")

    @property
    def b6_btn_hidden_locator(self) -> Locator:
        return self.page.locator("//button[@id='hidden-opacity']")
    
    @property
    def b6_btn_offscreen_locator(self) -> Locator:
        return self.page.locator("//button[@id='hidden-offscreen']")

    # 7
    @property
    def b7_text_locator(self) -> Locator:
        return self._text_locator.nth(3)

    # 7 - 1
    @property
    def b7_1_title_locator(self) -> Locator:
        return self.page.locator('.outer-label').first

    @property
    def b7_1_btn_locator(self) -> Locator:
        return self.page.locator('.outer-btn').first

    @property
    def b7_1_field_locator(self) -> Locator:
        return self.page.get_by_placeholder(self.const.h5_7_placeholder1)

    # 7 - 2
    @property
    def b7_2_title_locator(self) -> Locator:
        return self.page.locator('.inner-label').first

    @property
    def b7_2_btn_locator(self) -> Locator:
        return self.page.locator('.inner-btn').first

    @property
    def b7_2_field_locator(self) -> Locator:
        return self.page.get_by_placeholder(self.const.h5_7_placeholder2)

    # 7 - 3
    @property
    def b7_3_title_locator(self) -> Locator:
        return self.page.locator('.deep-label').first

    @property
    def b7_3_btn_locator(self) -> Locator:
        return self.page.locator('.deep-btn').first

    @property
    def b7_3_field_locator(self) -> Locator:
        return self.page.get_by_placeholder(self.const.h5_7_placeholder3)

    @property
    def b7_3_status_locator(self) -> Locator:
        return self.page.locator('#deep-status')
