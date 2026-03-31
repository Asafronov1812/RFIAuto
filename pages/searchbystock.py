from selenium.webdriver.common.by import By
import ConnectionsDB
from pages.searchbysections import SearchBySections
from psycopg2.extras import DictCursor
from psycopg2 import sql

class SearchByStock:
    # vars section 2.1
    agency_id = '3245240187931858924'
    title = 'Поиск разделов 2.1'
    title_element = 'h1[class="header header_h1 search-filter-block__header"]'
    search_button_element = 'button[class="button button_default button_primary search-page__button"]'
    reset_button_element = '[class="button button_default button_secondary search-page__button-secondary"]'

    def __init__(self, driver):
        self.driver = driver

    def open(self) :
        search_by_section = SearchBySections(self.driver)
        search_by_section.open()
        search_by_section.click_button_search_section('2.1. Сведения об акциях')

    def check_page_is_opened(self):
        page_title = self.driver.find_element(By.CSS_SELECTOR, self.title_element).text
        assert page_title == self.title, 'Не удалось открыть страницу'

    def click_button_search(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_button_element).click()

    def click_button_reset(self):
        self.driver.find_element(By.CSS_SELECTOR, self.reset_button_element).click()

#получаем из БД количество объектов для ТУ в статусах "Учтен" или "Исключен" по agency_id
    def get_count_of_object_from_db(self, agency_id = agency_id):
        with ConnectionsDB.conn.cursor(cursor_factory=DictCursor) as cursor:
            ConnectionsDB.conn.autocommit = True
            try:
                cursor.execute('SELECT count(*) FROM slice.registry_slice_card_stock '
                               'WHERE agency_id = %(id)s',
                               {'id': agency_id})
            except Exception:
                print('_ERROR!!! Could not get count of object from DB')
            for row in cursor:
                count = row[0]
            return count
