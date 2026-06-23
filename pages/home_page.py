from playwright.async_api import Page, expect

from pages.base_page import BasePage
from config.locators import HomePageLocators
from config.const import HomePageConst


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = HomePageLocators(self.page)
        self.const = HomePageConst()

    async def check_text(
            self,
    ) -> bool:
        title = self.locators.title_locator
        quotes = self.locators.quotes_locator
        author = self.locators.author_locator
        purpose = self.locators.purpose_locator
        text = self.locators.text_locator

        await expect(title).to_have_text(self.const.h1_text)
        await expect(quotes).to_have_text(self.const.quote)
        await expect(author).to_have_text(self.const.author)
        await expect(purpose).to_have_text(self.const.purpose_text)
        await expect(text).to_have_text(self.const.text)

    async def _check_block_title(
            self,
            data: str,
            number: int,
    ) -> bool:
        locator = self.locators.card_title_locator(number)
        await expect(locator).to_have_text(data)

    async def _check_block_description(
            self,
            data: str,
            number: int,
    ) -> bool:
        locator = self.locators.card_description_locator(number)
        await expect(locator).to_have_text(data)

    async def check_block_data(
            self,
            title: str,
            description: str,
            number: int,
    ) -> bool:
        number += 2
        if number > await self.locators.cards_locator.count():
            return False

        await self._check_block_title(title, number)
        await self._check_block_description(description, number)

    async def check_image(self) -> bool:
        locator = self.locators.img_locator
        await expect(locator).to_have_attribute('alt', self.const.img_alt)

    async def check_image_text(self) -> bool:
        locator = self.locators.img_text_locator
        await expect(locator).to_have_text(self.const.img_text)
