import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pages.homepage import HomePage
from pages.mainmenu import MainMenu
from pages.pagedata import settings



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

# фикстура ниже работает на всю сессию тестов, то есть вначале первого и в конце последнего
# @pytest.fixture(scope='session')
# def separator():
#     print('\ntest started')
#     yield 'value'
#     print('\ntest finished')

