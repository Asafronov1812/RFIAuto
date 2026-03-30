import time
import pytest
from selenium.webdriver.common.by import By
from pages.searchbybuilding import SearchByBuilding
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
def test_search_by_building_is_opened(driver):
    search = SearchByBuilding(driver)
    search.open()
    search.check_page_is_opened()

@pytest.mark.smoke
def test_building_count(driver):
    search = SearchByBuilding(driver)
    search.open()
    search.click_button_search()
    wait = WebDriverWait(driver, 60)
    wait.until_not(
        EC.text_to_be_present_in_element_attribute(
            (By.CSS_SELECTOR, 'button[class="button button_default button_primary search-page__button"]'),
            'class',                            # атрибут в котором ожидаем
            'button_loading'               # значение атрибута, которое ожидаем, что будет отсутствовать
        )
    )
    result_obj_count = driver.find_element(By.CSS_SELECTOR, '[class="counter-block__counter"]').text
    count_from_db = str(search.get_count_of_object_from_db(agency_id='3245240187931858924'))
    assert result_obj_count == count_from_db