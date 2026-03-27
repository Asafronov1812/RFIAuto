import time
import pytest
from selenium.webdriver.common.by import By
from pages.searchbyland import SearchByLand
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.skip
def test_search_by_land_is_opened(driver):
    search_by_land = SearchByLand(driver)
    search_by_land.open()
    search_by_land.check_page_is_opened()


def test_land_count(driver):
    search_by_land = SearchByLand(driver)
    search_by_land.open()
    search_by_land.click_button_search()
    wait = WebDriverWait(driver, 60)
    wait.until_not(
        EC.text_to_be_present_in_element_attribute(
            (By.CSS_SELECTOR, 'button[class="button button_default button_primary search-page__button"]'),
            'class',                            # атрибут в котором ожидаем
            'button_loading'               # значение атрибута, которое ожидаем, что будет отсутствовать
        )
    )
    result_obj_count = driver.find_element(By.CSS_SELECTOR, '[class="counter-block__counter"]').text
    assert result_obj_count == '367'
