import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pages.pagedata import settings
from pages.homepage import HomePage
from pages.mainmenu import MainMenu
from pages.generalsearchbysection import (SearchByLand, SearchByBuilding, SearchByRoom, SearchByShip,
                                          SearchByStock, SearchByInvestment, SearchByMovable, SearchByTransport,
                                          SearchByOtherMove, SearchByShare, SearchByHolder, SearchByChangeRecord,
                                          SearchByRequest, SearchByRFI)
from pages.searchbysections import SearchBySections


@pytest.fixture()
def driver() -> webdriver.Firefox:
    options = Options()
    #options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture()
def jwt_token():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture()
def page_home(driver):
    return HomePage(driver, *settings.page_home_set)

@pytest.fixture()
def page_mainmenu(driver):
    return MainMenu(driver, *settings.page_main_menu_set)

@pytest.fixture()
def page_search_by_section(driver):
    return SearchBySections(driver, *settings.page_search_by_sections_set)

@pytest.fixture()
def page_search_by_land(driver):
    return SearchByLand(driver, *settings.page_search_by_land_set)

@pytest.fixture()
def page_search_by_building(driver):
    return SearchByBuilding(driver, *settings.page_search_by_building_set)

@pytest.fixture()
def page_search_by_room(driver):
    return SearchByRoom(driver, *settings.page_search_by_room_set)

@pytest.fixture()
def page_search_by_ship(driver):
    return SearchByShip(driver, *settings.page_search_by_ship_set)

@pytest.fixture()
def page_search_by_stock(driver):
    return SearchByStock(driver, *settings.page_search_by_stock_set)

@pytest.fixture()
def page_search_by_investment(driver):
    return SearchByInvestment(driver, *settings.page_search_by_investment_set)

@pytest.fixture()
def page_search_by_movable(driver):
    return SearchByMovable(driver, *settings.page_search_by_movable_set)

@pytest.fixture()
def page_search_by_transport(driver):
    return SearchByTransport(driver, *settings.page_search_by_transport_set)

@pytest.fixture()
def page_search_by_other_move(driver):
    return SearchByOtherMove(driver, *settings.page_search_by_other_move_set)

@pytest.fixture()
def page_search_by_share(driver):
    return SearchByShare(driver, *settings.page_search_by_share_set)

@pytest.fixture()
def page_search_by_holder(driver):
    return SearchByHolder(driver, *settings.page_search_by_holder_set)

@pytest.fixture()
def page_search_by_change_record(driver):
    return SearchByChangeRecord(driver, *settings.page_search_by_change_record_set)

@pytest.fixture()
def page_search_by_request(driver):
    return SearchByRequest(driver, *settings.page_search_by_request_set)

@pytest.fixture()
def page_search_by_rfi(driver):
    return SearchByRFI(driver, *settings.page_search_by_rfi_set)



# фикстура ниже работает на всю сессию тестов, то есть вначале первого и в конце последнего
# @pytest.fixture(scope='session')
# def separator():
#     print('\ntest started')
#     yield 'value'
#     print('\ntest finished')

