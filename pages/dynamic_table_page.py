from playwright.sync_api import Page, expect
import logging

from pages.base_page import BasePage
from config.locators import DynamicTableLocators
from config.const import DynamicTableConst

logger = logging.getLogger(__name__)


class DynamicTablePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = DynamicTableLocators(self.page)
        self.const = DynamicTableConst()

    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(h4_2).to_have_text(self.const.h4_title2)

    def check_is_data_as_expected(self) -> bool:

        # Get locators
        expected_cpu_locator = self.locators.expected_result_locator
        head_cells_locator = self.locators.header_cell_locators
        row_locator = self.locators.table_row_locators

        # wait till load
        expect(row_locator.first).to_be_visible()

        # Find CPU line
        logger.debug('Cells count %s', head_cells_locator.count())
        cells_amount = head_cells_locator.count()

        for i in range(0, cells_amount):
            column_content = head_cells_locator.nth(i).text_content()
            logger.debug('column data: %s', column_content)
            if self.const.column in column_content:
                column = i
                break

        # Find Chrome row in table
        rows_amount = row_locator.count()
        logger.debug('Rows amount: %s', rows_amount)

        for i in range(0, rows_amount):
            row_content = row_locator.nth(i).text_content()
            logger.debug('COLUMN CONTENT = [%s]', row_content)
            if self.const.browser in row_content:
                row = i
                logger.debug('Expected row: %s', row)
                break

        # Get Actual Chrome CPU
        actual_locator = self.locators.table_cell_in_row_locators(row).nth(
            column)
        actual_result = actual_locator.text_content()

        # Check
        expect(expected_cpu_locator).to_have_text(
            self.const.expected_text.format(actual_result))
