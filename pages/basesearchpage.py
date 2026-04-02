from abc import abstractmethod
import allure
from selenium.webdriver.common.by import By
import ConnectionsDB
from page_factory.button import Button
from page_factory.counter import Counter
from pages.basepage import BasePage
from pages.pagedata import settings
from pages.searchbysections import SearchBySections
from psycopg2.extras import DictCursor
from psycopg2 import sql
from tests.testdata import search_data

class BaseSearchPage(BasePage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)
        self.button_search = Button(self.driver,
                                    (By.CSS_SELECTOR, 'button[class="button button_default button_primary search-page__button"]'),
                                    'Поиск')
        self.button_reset = Button(self.driver,
                                    (By.CSS_SELECTOR, '[class="button button_default button_secondary search-page__button-secondary"]'),
                                    'Сброс')
        self.button_export = Button(self.driver,
                                   (By.CSS_SELECTOR,
                                    'button[class="button button_default button_secondary search-page__button"]'),
                                   'Выгрузить Excel')
        self.counter = Counter(self.driver,
                                   (By.CSS_SELECTOR, '[class="counter-block__counter"]'),
                                   'Количество найденных объектов')

    @property
    @abstractmethod
    def db_table(self) -> str:
        return 'Base'

    @property
    @abstractmethod
    def section(self) -> str:
        return 'Base'

    @property
    @abstractmethod
    def object_type(self) -> str:
        return 'Base'

    def open(self) :
        with allure.step(f'Opening the search by {self.object_type} page'):
            search_by_sections = SearchBySections(self.driver, *settings.page_search_by_sections_set)
            search_by_sections.open()
            search_by_sections.click_button_search_section(self.section)

#получаем из БД количество объектов для ТУ в статусах "Учтен" или "Исключен" по agency_id
    def get_count_of_object_from_db(self, filter_param = search_data.sql_default_param):
        request = f"SELECT count(*) FROM {self.db_table} WHERE 1=1 {filter_param}"
        with allure.step(f'Getting count of object from DB by request: {request}'):
            with ConnectionsDB.conn.cursor(cursor_factory=DictCursor) as cursor:
                ConnectionsDB.conn.autocommit = True
                try:
                    cursor.execute(request)
                except Exception:
                    print('_ERROR!!! Could not get count of object from DB')
                for row in cursor:
                    count = row[0]
                return count