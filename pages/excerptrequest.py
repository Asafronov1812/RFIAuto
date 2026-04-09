import re
from abc import abstractmethod
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ConnectionsDB
from page_factory.button import Button
from page_factory.counter import Counter
from page_factory.datepicker import DatePicker
from page_factory.infofield import InfoField
from page_factory.input import Input
from page_factory.page import Page
from page_factory.selector import Selector
from page_factory.table import Table
from pages.basepage import BasePage
from pages.mainmenu import MainMenu
from pages.pagedata import settings
from psycopg2.extras import DictCursor
from psycopg2 import sql
from tests.testdata import search_data


class ExcerptRequestSearch(BasePage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)
        self.button_create_request = Button(self.driver,
                                    (By.CSS_SELECTOR,
                                     'button[class="button button_default button_primary buttons-block-rfi-request-search-page__button"]'),
                                    'Поиск')
        self.button_search = Button(self.driver,
                                    (By.CSS_SELECTOR, 'button[class="button button_default button_secondary buttons-block-rfi-request-search-page__button-secondary"]'),
                                    'Поиск')
        self.button_reset = Button(self.driver,
                                    (By.CSS_SELECTOR, '[class="button button_default button_secondary buttons-block-rfi-request-search-page__button-secondary"]'),
                                    'Сброс')
        self.button_export = Button(self.driver,
                                   (By.CSS_SELECTOR,
                                    'button[class="button button_default button_secondary buttons-block-rfi-request-search-page__button-secondary"]'),
                                   'Выгрузить Excel')
        self.counter = Counter(self.driver,
                                   (By.XPATH, '//div[starts-with(text(), "Записи")]'),
                                   'Количество найденных запросов')
        self.table_sent_requests = Table(self.driver,
                                         (By.XPATH, '//div[@class="rfi-sent-request-table"]//div[contains(@class, "table__container")]'),
                                         'Направленные запросы')
        self.input_number_of_request = Input(self.driver,
                                             (By.XPATH, '//*[text()="Номер запроса"]/parent::*/following-sibling::div//input'),
                                             'Номер запроса')

    @property
    @abstractmethod
    def db_table(self) -> str:
        return 'excerpt.request'

    @property
    @abstractmethod
    def section(self) -> str:
        return 'Запросы на предоставление выписок РФИ'

    @property
    @abstractmethod
    def object_type(self) -> str:
        return 'excerpt'

    def open(self) :
        with allure.step(f'Opening the search by excerpt-request page'):
            main_menu = MainMenu(self.driver, *settings.page_main_menu_set)
            main_menu.open()
            main_menu.click_button_select('Предоставление')

#получаем из БД количество выписок для ТУ по agency_id
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

class ExcerptRequestCreate(BasePage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)
        self.button_send = Button(self.driver,        # кнопка "Направить"
                                    (By.CSS_SELECTOR,
                                     'button[class="button button_default button_primary rfi-control-buttons-block__big-wrapper-button"]'),
                                    'Направить')
        self.button_cancel = Button(self.driver,  # кнопка "Отмена"
                                    (By.CSS_SELECTOR,
                                     'div[class="rfi-control-buttons-block"] button[class="button button_default button_secondary"]'),
                                    'Отмена')
        self.button_cancel_modal = Button(self.driver,  # кнопка "Отмена" в модалке поиска объектов
                                    (By.CSS_SELECTOR,
                                     'div[class="modal__footer"] button[class="button button_default button_secondary"]'),
                                    'Отмена')
        self.button_add_object = Button(self.driver,   # кнопка "Добавить объекты"
                                    (By.CSS_SELECTOR,
                                     'button[class="button button_default button_ghost rfi-request-table__add-applicant"]'),
                                    'Добавить объект запроса')
        self.selector_applicant = Selector(self.driver,
                               (By.CSS_SELECTOR, 'input[id="react-select-2-input"]'),
                               'Заявитель')
        self.input_incoming_document_number = Input(self.driver,
                               (By.CSS_SELECTOR, '[name="incomingDocumentNumber"]'),
                               'Номер входящего')
        self.datepiker_incoming_date = DatePicker(self.driver,
                               (By.CSS_SELECTOR, 'input[name="incomingDocumentDate"]'),
                               'Дата входящего')
        self.button_search = Button(self.driver,
                                    (By.CSS_SELECTOR, 'button[class~="modal-body-content__button"]'),
                                    'Поиск')
        self.button_reset = Button(self.driver,
                                    (By.CSS_SELECTOR, 'button[class="button button_default button_secondary modal-body-content__button-secondary"]'),
                                    'Сброс')
        self.button_choose = Button(self.driver,
                                    (By.CSS_SELECTOR, 'button[class="button button_default button_primary"]'),
                                    'Выбрать')
        self.table_objects = Table(self.driver,
                                         (By.XPATH, '//table[contains(@class, "modal-body-content__table")]/parent::*'),
                                         'Объекты РФИ для добавления к запросу выписки РФИ')
        self.page_excerpt_request = Page(self.driver, (By.CSS_SELECTOR, 'body'), 'Страница создания запроса на выписку РФИ')


    @property
    @abstractmethod
    def db_table(self) -> str:
        return 'excerpt.request'

    @property
    @abstractmethod
    def section(self) -> str:
        return 'Запрос на предоставление выписок РФИ'

    @property
    @abstractmethod
    def object_type(self) -> str:
        return 'create excerpt request'

    def open(self) :
        with allure.step(f'Opening the create excerpt request page'):
            excerpt_request = ExcerptRequestSearch(self.driver, *settings.page_main_menu_set)
            excerpt_request.open()
            excerpt_request.button_create_request.click()


class ExcerptRequest(BasePage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)
        # self.button_send = Button(self.driver,
        #                             (By.CSS_SELECTOR,
        #                              'button[class="button button_default button_primary rfi-control-buttons-block__big-wrapper-button"]'),
        #                             'Направить')
        self.button_cancel = Button(self.driver,
                                    (By.CSS_SELECTOR,
                                     'button[class="button button_default button_secondary"]'),
                                    'Закрыть')
        self.input_outgoing_document_number = Input(self.driver,
                               (By.CSS_SELECTOR, 'input[name="outgoingDocumentNumber"]'),
                               'Номер исходящего')
        self.datepicker_outgoing_date = DatePicker(self.driver,
                               (By.CSS_SELECTOR, 'input[name="outgoingDocumentDate"]'),
                               'Дата исходящего')
        self.info_field_status = InfoField(self.driver, (By.CSS_SELECTOR, 'span[class~="tag_statusCode"]'),
                                           'Статус запроса')
        self.button_generate = Button(self.driver,
                                    (By.XPATH,
                                     '//span[text() = "Сформировать выписки"]/ancestor::button'),
                                    'Сформировать выписки')
        self.button_generate_with_history = Button(self.driver,
                                    (By.XPATH,
                                     '//span[text() = "Сформировать выписки с историей"]/ancestor::button'),
                                    'Сформировать выписки с историей')
        self.button_refuse = Button(self.driver,
                                    (By.XPATH,
                                     '//span[text() = "Сформировать отказ"]/ancestor::button'),
                                    'Сформировать отказ')
        self.button_send_result = Button(self.driver,
                                    (By.XPATH,
                                     '//span[text() = "Направить результат"]/ancestor::button'),
                                    'Направить результат')
        self.page_request = Page(self.driver, (By.CSS_SELECTOR, 'body'), 'Запрос на выписку РФИ')


    @property
    @abstractmethod
    def db_table(self) -> str:
        return 'excerpt.request'

    @property
    @abstractmethod
    def section(self) -> str:
        return 'Запрос на предоставление выписок РФИ'

    @property
    @abstractmethod
    def object_type(self) -> str:
        return 'excerpt'

    def get_request_number(self) -> str:
        with allure.step(f'Getting the excerpt request number'):
           title = self.driver.find_element(*self.title_locator).text
           request_number = re.findall(r"\d+", title)
           return request_number[0]