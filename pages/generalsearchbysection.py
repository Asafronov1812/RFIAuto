import allure
from selenium.webdriver.common.by import By

from page_factory.button import Button
from page_factory.dropdown import DropDown
from page_factory.input import Input
from pages.basesearchpage import BaseSearchPage
from pages.mainmenu import MainMenu
from pages.pagedata import settings


class SearchByLand(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_land'

    @property
    def section(self) -> str:
        return '1.1. Сведения о земельных участках'

    @property
    def object_type(self) -> str:
        return 'Land (1.1)'

class SearchByBuilding(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_building'

    @property
    def section(self) -> str:
        return '1.2. Сведения о зданиях, сооружениях, объектах незавершенного строительства, единых недвижимых комплексах'

    @property
    def object_type(self) -> str:
        return 'Building (1.2)'

class SearchByRoom(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_room'

    @property
    def section(self) -> str:
        return '1.3. Сведения о помещениях, машино-местах'

    @property
    def object_type(self) -> str:
        return 'Room (1.3)'

class SearchByShip(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_ship'

    @property
    def section(self) -> str:
        return '1.4. Сведения о воздушных и морских судах, судах внутреннего плавания'

    @property
    def object_type(self) -> str:
        return 'Ship (1.4)'

class SearchByStock(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_stock'

    @property
    def section(self) -> str:
        return '2.1. Сведения об акциях'

    @property
    def object_type(self) -> str:
        return 'Stock (2.1)'

class SearchByInvestment(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_investment'

    @property
    def section(self) -> str:
        return '2.2. Сведения о долях (вкладах) в уставных (складочных) капиталах хозяйственных обществ и товариществ'

    @property
    def object_type(self) -> str:
        return 'Investment (2.2)'

class SearchByMovable(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_movable'

    @property
    def section(self) -> str:
        return ('2.3. Сведения о движимом имуществе, первоначальная стоимость которого равна '
                'или превышает 500 тыс. руб, особо ценном имуществе, первоначальная стоимость которого равна '
                'или превышает 200 тыс. руб, и ином имуществе')

    @property
    def object_type(self) -> str:
        return 'Movable (2.3)'

class SearchByTransport(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_transport'

    @property
    def section(self) -> str:
        return ('2.4. Сведения о транспортных средствах')

    @property
    def object_type(self) -> str:
        return 'Transport (2.4)'

class SearchByOtherMove(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_other_move'

    @property
    def section(self) -> str:
        return ('2.5. Сведения об ином движимом имуществе, первоначальная стоимость единицы которого '
                'меньше 500 тыс. руб, за исключением имущества, обращенного в собственность РФ, '
                'а также особо ценном движимом имуществе, первоначальная стоимость единицы которого '
                'меньше 200 тыс. руб, и оборотных активах (независимо от их стоимости), '
                'учитываемых как единые объекты')

    @property
    def object_type(self) -> str:
        return 'OtherMove (2.5)'

class SearchByShare(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_share'

    @property
    def section(self) -> str:
        return ('2.6. Сведения о долях в праве общей долевой собственности на объекты недвижимого и (или) '
                'движимого имущества, за исключением имущества, обращенного в собственность РФ')

    @property
    def object_type(self) -> str:
        return 'Share (2.6)'

class SearchByHolder(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_holder'

    @property
    def section(self) -> str:
        return ('3.1 Сведения о правообладателях объектов учета')

    @property
    def object_type(self) -> str:
        return 'Holder (3.1)'

class SearchByChangeRecord(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)
        self.button_search = Button(self.driver,
                                    (By.CSS_SELECTOR, 'button[class="button button_default button_primary mix split is has state toString"]'),
                                    'Поиск')
        self.button_reset = Button(self.driver,
                                    (By.CSS_SELECTOR, '[class="button button_default button_secondary mix split is has state toString"]'),
                                    'Сброс')

    @property
    def db_table(self) -> str:
        return 'request_processing.v_get_change_record_search'

    @property
    def section(self) -> str:
        return 'Поиск по записям'

    @property
    def object_type(self) -> str:
        return 'Change record'

    def open(self) :
        with allure.step(f'Opening the search by {self.object_type} page'):
            main_menu = MainMenu(self.driver, *settings.page_main_menu_set)
            main_menu.open()
            main_menu.click_button_select(self.section)

class SearchByRequest(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)
        self.button_search = Button(self.driver,
                                    (By.CSS_SELECTOR, 'button[class="button button_default button_primary search-request-page__button"]'),
                                    'Поиск')
        self.button_reset = Button(self.driver,
                                    (By.CSS_SELECTOR, '[class="button button_default button_secondary search-request-page__button-secondary"]'),
                                    'Сброс')

    @property
    def db_table(self) -> str:
        return 'request_processing.v_get_request_search'

    @property
    def section(self) -> str:
        return 'Поиск по запросам'

    @property
    def object_type(self) -> str:
        return 'Request'

    def open(self) :
        with allure.step(f'Opening the search by {self.object_type} page'):
            main_menu = MainMenu(self.driver, *settings.page_main_menu_set)
            main_menu.open()
            main_menu.click_button_select(self.section)

class SearchByRFI(BaseSearchPage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)
        self.button_search = Button(self.driver,
                                    (By.CSS_SELECTOR, 'button[class="button button_default button_primary search-federal-property-register-page__button"]'),
                                    'Поиск')
        self.button_reset = Button(self.driver,
                                    (By.CSS_SELECTOR, 'button[class="button button_default button_secondary search-federal-property-register-page__button-secondary"]'),
                                    'Сброс')
        self.input_section_rfi = Input(self.driver,
                                       (By.XPATH, '//*[text()="Раздел РФИ"]/parent::*/following-sibling::div'),
                                       'Раздел РФИ')
        self.dropdown_section_rfi = DropDown(self.driver,
                                       (By.CSS_SELECTOR, 'div[class="react-select__menu css-1nmdiq5-menu"]'),
                                       'Раздел РФИ')
        self.input_section_status = Input(self.driver,
                                          (By.XPATH, '//*[text()="Статус раздела"]/parent::*/following-sibling::div'),
                                          'Статус раздела')
        self.input_section_tu = Input(self.driver,
                                          (By.XPATH, '//*[text()="Территориальный орган Росимущества"]/parent::*/following-sibling::div'),
                                          'Территориальный орган Росимущества')
        self.dropdown_tu = DropDown(self.driver,
                                       (By.CSS_SELECTOR, 'div[class="react-select__menu css-1nmdiq5-menu"]'),
                                       'Территориальный орган Росимущества')

    @property
    def db_table(self) -> str:
        return 'slice.registry_slice_card_land'

    @property
    def section(self) -> str:
        return 'Поиск в Реестре федерального имущества'

    @property
    def object_type(self) -> str:
        return 'RFI'

    def open(self) :
        with allure.step(f'Opening the search by {self.object_type} page'):
            main_menu = MainMenu(self.driver, *settings.page_main_menu_set)
            main_menu.open()
            main_menu.click_button_select(self.section)