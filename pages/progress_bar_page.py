from playwright.sync_api import Page, expect
import time
import logging

from pages.base_page import BasePage
from config.locators import ProgressBarLocators
from config.const import ProgressBarConst

logger = logging.getLogger(__name__)


class ProgressBarPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ProgressBarLocators(self.page)
        self.const = ProgressBarConst()

    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text = self.locators.text_locator
        h4_1 = self.locators.h4_title_locator(1)
        bullet = self.locators.bullet_locators(1)
        h4_2 = self.locators.h4_title_locator(2)
        btn1 = self.locators.start_btn_locator
        btn2 = self.locators.stop_btn_locator
        result = self.locators.result_locator

        expect(h3).to_have_text(self.const.h3)
        expect(text).to_have_text(self.const.text)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet).to_have_text(self.const.bullet)
        expect(h4_2).to_have_text(self.const.h4_title2)
        expect(btn1).to_have_text(self.const.btn_start)
        expect(btn2).to_have_text(self.const.btn_stop)
        expect(result).to_have_text(self.const.default_result)

    def progress_bar_actions(
            self,
            expected_progress: int,
    ) -> bool:
        expected_progress_txt = f'{expected_progress}%'

        # Locators
        progress_locator = self.locators.progress_bar_locator
        start_btn_locator = self.locators.start_btn_locator
        stop_btn_locator = self.locators.stop_btn_locator
        result_locator = self.locators.result_locator

        # Actions
        start_btn_locator.click()
        start_time = time.perf_counter()

        while True:
            progress_txt = progress_locator.text_content()

            if progress_txt == expected_progress_txt:
                break

            time.sleep(0.01)

        stop_btn_locator.click()
        elapsed = time.perf_counter() - start_time
        elapsed = str(elapsed).replace('0.', '').replace('.', '')
        elapsed = elapsed[:4]

        # counting
        result = expected_progress - 75
        actual_time = result_locator.text_content()[-5:]
        logger.debug('Actual time: %s, Expected time: %s',
                     actual_time, elapsed)

        # Check
        expect(result_locator).to_contain_text(self.const.result.format(
            result,
        ))
        assert (int(elapsed) - int(actual_time)) < 1000
