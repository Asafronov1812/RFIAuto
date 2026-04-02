from pages.basesearchpage import BaseSearchPage


class SearchByLand(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_land'

    @property
    def section(self) -> str:
        return '1.1. Сведения о земельных участках'