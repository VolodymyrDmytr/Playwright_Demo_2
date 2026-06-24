from playwright.sync_api import Page, expect
import allure

from config.const import BaseConstants
from config.locators import BaseLocators


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.locators = BaseLocators(self.page)
        self.const = BaseConstants()

    @allure.step('Open home page')
    def open_base_page(self) -> None:
        self.page.goto(self.const.base_url)

    @allure.step('Check is page title: {data}')
    def check_page_title(
            self,
            data: str,
    ) -> bool:
        """Check is page title as expected

        Args:
            data (str): expected page title

        Returns:
            bool: True, if page title is as expected
        """
        expect(self.page).to_have_title(data)

    @allure.step('Check is page url: {data}')
    def check_url(
            self,
            data: str,
    ) -> bool:
        """Check is page URL as expected

        Args:
            data (str): expected page URL

        Returns:
            bool: True, if page URL is as expected
        """
        expect(self.page).to_have_url(data)

    @allure.step('Click on link: {data}')
    def click_on_link(
            self,
            data: str,
    ) -> None:
        """Click on link with text

        Args:
            data (str): link text
        """
        self.locators.link_locator(data).click()
