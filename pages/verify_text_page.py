from playwright.sync_api import Page, expect
import logging
import allure

from pages.base_page import BasePage
from config.locators import VerifyTextLocators
from config.const import VerifyTextConst

logger = logging.getLogger(__name__)


class VerifyTextPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = VerifyTextLocators(self.page)
        self.const = VerifyTextConst()

    @allure.step('Verify page content is correct')
    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text1 = self.locators.text_locators(1)
        fake_text1 = self.locators.find_text(1)
        text2 = self.locators.text_locators(3)
        fake_text2 = self.locators.find_text(2)
        text3 = self.locators.text_locators(5)
        table_title1 = self.locators.table_locators(1)
        xpath1 = self.locators.table_locators(3)
        table_title2 = self.locators.table_locators(2)
        xpath2 = self.locators.table_locators(4)
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        h4_2 = self.locators.h4_title_locator(2)
        text_to_find = self.locators.find_text(4)

        expect(h3).to_have_text(self.const.h3)
        expect(text1).to_have_text(self.const.text1)
        expect(fake_text1).to_have_text(self.const.fake_text)
        expect(text2).to_have_text(self.const.text2)
        expect(fake_text2).to_have_text(self.const.fake_text)
        expect(text3).to_have_text(self.const.text3)
        expect(table_title1).to_have_text(self.const.table_title1)
        expect(xpath1).to_have_text(self.const.xpath1)
        expect(table_title2).to_have_text(self.const.table_title2)
        expect(xpath2).to_have_text(self.const.xpath2)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(h4_2).to_have_text(self.const.h4_title2)
        expect(text_to_find).to_have_text(self.const.text_to_find)

    @allure.step('Find text')
    def find_text(self) -> bool:
        locator = self.locators.find_by_text(self.const.text_to_find)
        logger.debug('Actual text: %s', locator.text_content())
        expect(locator).to_have_text(self.const.text_to_find)
        # check to make shure that right element was found
