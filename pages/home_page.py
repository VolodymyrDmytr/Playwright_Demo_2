from playwright.sync_api import Page, expect
import allure

from pages.base_page import BasePage
from config.locators import HomePageLocators
from config.const import HomePageConst


class HomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = HomePageLocators(self.page)
        self.const = HomePageConst()

    @allure.step('Verify page content is correct')
    def check_text(
            self,
    ) -> bool:
        title = self.locators.title_locator
        quotes = self.locators.quotes_locator
        author = self.locators.author_locator
        purpose = self.locators.purpose_locator
        text = self.locators.text_locator

        expect(title).to_have_text(self.const.h1_text)
        expect(quotes).to_have_text(self.const.quote)
        expect(author).to_have_text(self.const.author)
        expect(purpose).to_have_text(self.const.purpose_text)
        expect(text).to_have_text(self.const.text)

    def _check_block_title(
            self,
            data: str,
            number: int,
    ) -> bool:
        locator = self.locators.card_title_locator(number)
        expect(locator).to_have_text(data)

    def _check_block_description(
            self,
            data: str,
            number: int,
    ) -> bool:
        locator = self.locators.card_description_locator(number)
        expect(locator).to_have_text(data)

    @allure.step('Check is block {number} contains {title}, {description}')
    def check_block_data(
            self,
            title: str,
            description: str,
            number: int,
    ) -> bool:
        number += 2
        if number > self.locators.cards_locator.count():
            return False

        self._check_block_title(title, number)
        self._check_block_description(description, number)

    @allure.step('Check is image correct')
    def check_image(self) -> bool:
        locator = self.locators.img_locator

        expect(locator).to_have_attribute('alt', self.const.img_alt)

    @allure.step('Check image text')
    def check_image_text(self) -> bool:
        locator = self.locators.img_text_locator
        expect(locator).to_have_text(self.const.img_text)
