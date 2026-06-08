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
