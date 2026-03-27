import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# https://www.youtube.com/watch?v=FNQil1Qzghk&list=PLRVGb5te8vVH3DJKxtRQp3-68_gQ3CEqx&index=6

@pytest.fixture()
def driver():
    options = Options()
    #options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# фикстура ниже работает на всю сессию тестов, то есть вначале первого и в конце последнего
# @pytest.fixture(scope='session')
# def separator():
#     print('\ntest started')
#     yield 'value'
#     print('\ntest finished')

