from playwright.sync_api import Page, expect, Locator
import allure

from pages.base_page import BasePage
from config.locators import MouseOverLocators
from config.const import MouseOverConst


class MouseOverPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = MouseOverLocators(self.page)
        self.const = MouseOverConst()

    @allure.step('Verify page content is correct')
    def check_page_content(self) -> bool:
        h3 = self.locators.h3_locator
        text1 = self.locators.text_locators(1)
        text2 = self.locators.text_locators(2)
        h4_1 = self.locators.h4_title_locator(1)
        bullet1 = self.locators.bullet_locators(1)
        bullet2 = self.locators.bullet_locators(2)
        h4_2 = self.locators.h4_title_locator(2)
        text3 = self.locators.text_locators(3)
        text5 = self.locators.text_locators(5)

        expect(h3).to_have_text(self.const.h3)
        expect(text1).to_have_text(self.const.text1)
        expect(text2).to_have_text(self.const.text2)
        expect(h4_1).to_have_text(self.const.h4_title1)
        expect(bullet1).to_have_text(self.const.bullet1)
        expect(bullet2).to_have_text(self.const.bullet2)
        expect(h4_2).to_have_text(self.const.h4_title2)
        expect(text3).to_have_text(self.const.text3)
        expect(text5).to_have_text(self.const.text5)

    @allure.step('Click on link {data} - {clicks_amount} times')
    def click_on_link_p(
            self,
            data: int,
            clicks_amount: int,
    ) -> None:
        """Click on one of the links

        Args:
            data (int): 1 / 2
        """
        active_link = self.locators.link_page_locator(data)
        hover_link = self.locators.link_on_hover_locator

        active_link.hover()

        for _ in range(0, clicks_amount):
            hover_link.click()

    @allure.step('Check is {data} link was cliked {clicks_amount} times')
    def check_amount_of_clicks_for_link(
            self,
            data: int,
            clicks_amount: int,
    ) -> bool:
        if data == 1:
            data = self.const.text4_counter.format(clicks_amount)
            locator = self.locators.text_locators(4)
        elif data == 2:
            data = self.const.text6_counter.format(clicks_amount)
            locator = self.locators.text_locators(6)
        else:
            data = ''
            locator = Locator()

        expect(locator).to_have_text(data)
