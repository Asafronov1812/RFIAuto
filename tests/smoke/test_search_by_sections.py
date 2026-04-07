import allure
import pytest


@allure.feature('Страницы поиска')
@allure.story('Страница с выбором раздела для поиска')
@pytest.mark.smoke
def test_search_by_sections(page_search_by_section) :
    page_search_by_section.open()
    page_search_by_section.check_page_is_opened()
    page_search_by_section.check_section_count()

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по земле')
@pytest.mark.smoke
def test_search_by_land(page_search_by_land):
    page_search_by_land.open()
    page_search_by_land.check_page_is_opened()
    page_search_by_land.button_search.click()
    page_search_by_land.button_search.wait_for_load()
    count_from_db = page_search_by_land.get_count_of_object_from_db()
    page_search_by_land.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_land.button_reset.click()
    page_search_by_land.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по зданиям')
@pytest.mark.smoke
def test_search_by_building(page_search_by_building):
    page_search_by_building.open()
    page_search_by_building.check_page_is_opened()
    page_search_by_building.button_search.click()
    page_search_by_building.button_search.wait_for_load()
    count_from_db = page_search_by_building.get_count_of_object_from_db()
    page_search_by_building.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_building.button_reset.click()
    page_search_by_building.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по помещениям')
@pytest.mark.smoke
def test_search_by_room(page_search_by_room):
    page_search_by_room.open()
    page_search_by_room.check_page_is_opened()
    page_search_by_room.button_search.click()
    page_search_by_room.button_search.wait_for_load()
    count_from_db = page_search_by_room.get_count_of_object_from_db()
    page_search_by_room.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_room.button_reset.click()
    page_search_by_room.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по кораблям и самолетам')
@pytest.mark.smoke
def test_search_by_ship(page_search_by_ship):
    page_search_by_ship.open()
    page_search_by_ship.check_page_is_opened()
    page_search_by_ship.button_search.click()
    page_search_by_ship.button_search.wait_for_load()
    count_from_db = page_search_by_ship.get_count_of_object_from_db()
    page_search_by_ship.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_ship.button_reset.click()
    page_search_by_ship.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по акциям')
@pytest.mark.smoke
def test_search_by_stock(page_search_by_stock):
    page_search_by_stock.open()
    page_search_by_stock.check_page_is_opened()
    page_search_by_stock.button_search.click()
    page_search_by_stock.button_search.wait_for_load()
    count_from_db = page_search_by_stock.get_count_of_object_from_db()
    page_search_by_stock.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_stock.button_reset.click()
    page_search_by_stock.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по инвестициям')
@pytest.mark.smoke
def test_search_by_investment(page_search_by_investment):
    page_search_by_investment.open()
    page_search_by_investment.check_page_is_opened()
    page_search_by_investment.button_search.click()
    page_search_by_investment.button_search.wait_for_load()
    count_from_db = page_search_by_investment.get_count_of_object_from_db()
    page_search_by_investment.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_investment.button_reset.click()
    page_search_by_investment.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по движимому имуществу')
@pytest.mark.smoke
def test_search_by_movable(page_search_by_movable):
    page_search_by_movable.open()
    page_search_by_movable.check_page_is_opened()
    page_search_by_movable.button_search.click()
    page_search_by_movable.button_search.wait_for_load()
    count_from_db = page_search_by_movable.get_count_of_object_from_db()
    page_search_by_movable.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_movable.button_reset.click()
    page_search_by_movable.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по транспорту')
@pytest.mark.smoke
def test_search_by_transport(page_search_by_transport):
    page_search_by_transport.open()
    page_search_by_transport.check_page_is_opened()
    page_search_by_transport.button_search.click()
    page_search_by_transport.button_search.wait_for_load()
    count_from_db = page_search_by_transport.get_count_of_object_from_db()
    page_search_by_transport.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_transport.button_reset.click()
    page_search_by_transport.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по иному движимому имуществу')
@pytest.mark.smoke
def test_search_by_other_move(page_search_by_other_move):
    page_search_by_other_move.open()
    page_search_by_other_move.check_page_is_opened()
    page_search_by_other_move.button_search.click()
    page_search_by_other_move.button_search.wait_for_load()
    count_from_db = page_search_by_other_move.get_count_of_object_from_db()
    page_search_by_other_move.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_other_move.button_reset.click()
    page_search_by_other_move.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по долевому участию')
@pytest.mark.smoke
def test_search_by_share(page_search_by_share):
    page_search_by_share.open()
    page_search_by_share.check_page_is_opened()
    page_search_by_share.button_search.click()
    page_search_by_share.button_search.wait_for_load()
    count_from_db = page_search_by_share.get_count_of_object_from_db()
    page_search_by_share.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_share.button_reset.click()
    page_search_by_share.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по правообладателям')
@pytest.mark.smoke
def test_search_by_holder(page_search_by_holder):
    page_search_by_holder.open()
    page_search_by_holder.check_page_is_opened()
    page_search_by_holder.button_search.click()
    page_search_by_holder.button_search.wait_for_load()
    count_from_db = page_search_by_holder.get_count_of_object_from_db()
    page_search_by_holder.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_holder.button_reset.click()
    page_search_by_holder.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по записям на изменение')
@pytest.mark.smoke
def test_search_by_change_record(page_search_by_change_record):
    page_search_by_change_record.open()
    page_search_by_change_record.check_page_is_opened()
    page_search_by_change_record.button_search.click()
    page_search_by_change_record.button_search.wait_for_load()
    count_from_db = page_search_by_change_record.get_count_of_object_from_db()
    page_search_by_change_record.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_change_record.button_reset.click()
    page_search_by_change_record.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по запросам')
@pytest.mark.smoke
def test_search_by_request(page_search_by_request):
    page_search_by_request.open()
    page_search_by_request.check_page_is_opened()
    page_search_by_request.button_search.click()
    page_search_by_request.button_search.wait_for_load()
    count_from_db = page_search_by_request.get_count_of_object_from_db()
    page_search_by_request.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_request.button_reset.click()
    page_search_by_request.counter.should_have_text('0', 'Кнопка очистки не сработала')

@allure.feature('Страницы поиска')
@allure.story('Страница с поиском по реестру федерального имущества')
@pytest.mark.smoke
def test_search_by_rfi(page_search_by_rfi):
    page_search_by_rfi.open()
    page_search_by_rfi.check_page_is_opened()
    page_search_by_rfi.input_section_rfi.wait_for_enable()
    page_search_by_rfi.input_section_rfi.click()
    page_search_by_rfi.dropdown_section_rfi.click('Раздел 1.1 «Сведения о земельных участках»')
    page_search_by_rfi.input_section_tu.click()
    page_search_by_rfi.dropdown_tu.click('ТУ в Саратовской области')
    page_search_by_rfi.button_search.click()
    page_search_by_rfi.button_search.wait_for_load()
    count_from_db = page_search_by_rfi.get_count_of_object_from_db()
    page_search_by_rfi.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
    page_search_by_rfi.button_reset.click()
    page_search_by_rfi.counter.should_have_text('0', 'Кнопка очистки не сработала')