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


class DynamicIdLoators(BaseLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def button_locator(self) -> Locator:
        return self.page.locator('.btn-primary')

    @property
    def h3_title_locator(self) -> Locator:
        return self.page.locator('//h3')

    @property
    def text_locator(self) -> Locator:
        return self.page.locator('//p')

    @property
    def _h4_title_locators(self) -> Locator:
        return self.page.locator('//h4')

    @property
    def h4_title1_locator(self) -> Locator:
        return self._h4_title_locators.nth(0)

    @property
    def h4_title2_locator(self) -> Locator:
        return self._h4_title_locators.nth(1)

    def bullet_locator(self, number) -> Locator:
        number += 1
        return self.page.locator('//li').nth(number)


class ClassAttributeLocators(BaseLocators):

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

    @property
    def h3_title_locator(self) -> Locator:
        return self.page.locator('//h3')

    def text_locator(
            self,
            data: int,
    ) -> Locator | bool:
        data -= 1
        return self.page.locator('//p').nth(data)

    @property
    def _h4_title_locators(self) -> Locator:
        return self.page.locator('//h4')

    @property
    def h4_title1_locator(self) -> Locator:
        return self._h4_title_locators.nth(0)

    @property
    def h4_title2_locator(self) -> Locator:
        return self._h4_title_locators.nth(1)

    def bullet_locator(self, number) -> Locator:
        number += 1
        return self.page.locator('//li').nth(number)

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


class HiddenLayersLocators(BaseLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def btn_locator(self) -> Locator:
        return self.page.locator('.btn-success')

    @property
    def success_locator(self) -> Locator:
        return self.page.locator('.spa-view').nth(1)

    @property
    def h3_title_locator(self) -> Locator:
        return self.page.locator('//h3')

    @property
    def text_locator(self) -> Locator:
        return self.page.locator('//p')

    def h4_title_locator(
            self,
            data: int,
    ) -> Locator:
        data -= 1
        return self.page.locator('//h4').nth(data)

    def bullets_locator(
            self,
            data: int,
    ) -> Locator:
        data += 1
        return self.page.locator('//li').nth(data)


class LoadDelaysLocators(BaseLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def btn_locator(self) -> Locator:
        return self.page.locator('.btn-primary')

    @property
    def h3_locator(self) -> Locator:
        return self.page.locator('//h3')

    @property
    def text_locator(self) -> Locator:
        return self.page.locator('//p')

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
