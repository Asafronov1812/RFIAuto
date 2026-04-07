import time
import allure
import pytest
from selenium.webdriver.common.keys import Keys
from pages.excerptrequest import ExcerptRequestCreate, ExcerptRequest
from pages.pagedata import settings


@allure.feature('Выписки из РФИ')
@allure.story('Создание выписки')
@pytest.mark.smoke
def test_excerpt_rfi(page_excerpt_request_search):
    page_excerpt_request_search.open()
    page_excerpt_request_search.check_page_is_opened()
    page_excerpt_request_search.table_sent_requests.wait_for_load()
    page_excerpt_request_search.button_create_request.click()
    #далее переходим на страницу создания запроса
    page_excerpt_request_create = ExcerptRequestCreate(page_excerpt_request_search.driver, *settings.page_excerpt_request_create_set)
    page_excerpt_request_create.switch_to_tab(1)              #переключаемся на вторую вкладку со страницей создания запроса
    page_excerpt_request_create.check_page_is_opened()
    page_excerpt_request_create.datepiker_incoming_date.send_keys('01042026')
    page_excerpt_request_create.datepiker_incoming_date.send_keys(Keys.ENTER)
    page_excerpt_request_create.input_incoming_document_number.send_keys('автотест')
    page_excerpt_request_create.selector_applicant.send_keys('АКЦИОНЕРНОЕ ОБЩЕСТВО "ПОЧТА РОССИИ"')
    page_excerpt_request_create.selector_applicant.wait_for_load()
    page_excerpt_request_create.selector_applicant.send_keys(Keys.ENTER)
    #добавляем объект к запросу
    page_excerpt_request_create.button_add_object.click()
    page_excerpt_request_create.button_search.click()
    page_excerpt_request_create.button_search.wait_for_load()
    page_excerpt_request_create.table_objects.select_row(1)
    page_excerpt_request_create.table_objects.select_row(2)
    page_excerpt_request_create.table_objects.select_row(3)
    page_excerpt_request_create.button_choose.click()
    #направляем запрос на рассмотрение
    page_excerpt_request_create.button_send.click()
    page_excerpt_request_create.page_excerpt_request.wait_for_load()
    #инициализируем страницу запроса
    page_excerpt_request = ExcerptRequest(page_excerpt_request_create.driver, *settings.page_excerpt_request_set)
    page_excerpt_request.check_page_is_opened()
    page_excerpt_request.info_field_status.should_have_text('Принято от заявителя')
    #генерируем выписки и проверяем статус
    page_excerpt_request.button_generate.click()
    page_excerpt_request.page_request.wait_for_load()
    page_excerpt_request.info_field_status.should_have_text('Сформирован результат')
    #направляем ответ и проверяем получение конечного статуса
    page_excerpt_request.button_send_result.should_be_disabled()
    page_excerpt_request.datepicker_outgoing_date.send_keys('01042026')
    page_excerpt_request.datepicker_outgoing_date.send_keys(Keys.ENTER)
    page_excerpt_request.input_outgoing_document_number.send_keys('автотест-исходящий')
    page_excerpt_request.button_send_result.wait_for_enable()
    page_excerpt_request.button_send_result.should_be_enabled()
    page_excerpt_request.button_send_result.click()
    page_excerpt_request.page_request.wait_for_load()
    page_excerpt_request.info_field_status.should_have_text('Услуга оказана')
    #дальше проверяем, что созданный запрос ищется в реестре выписок
    request_number = page_excerpt_request.get_request_number()    # запоминаем номер созданного запроса
    page_excerpt_request.switch_to_tab(0)                          # переключаем вкладку на первую
    page_excerpt_request_search.check_page_is_opened()
    page_excerpt_request_search.input_number_of_request.send_keys(request_number)
    page_excerpt_request_search.button_search.click()
    page_excerpt_request_search.table_sent_requests.wait_for_load()
    page_excerpt_request_search.table_sent_requests.checking_row_with_param('Номер запроса', request_number, 1)
    # row = page_excerpt_request_search.table_sent_requests.get_row(1)
    # assert row['Номер запроса'] == request_number                 #сравниваем номер запроса с номером из таблицы