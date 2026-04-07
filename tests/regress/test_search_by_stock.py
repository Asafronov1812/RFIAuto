import pytest
from selenium.webdriver.common.by import By
from pages.searchbystock import SearchByStock
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.pagedata import page_elements as elem

@pytest.mark.smoke
def test_stock_count(driver):
    search = SearchByStock(driver)
    search.open()
    search.check_page_is_opened()
    search.click_button_search()
    wait = WebDriverWait(driver, 60)
    wait.until_not(
        EC.text_to_be_present_in_element_attribute(
            (By.CSS_SELECTOR, elem.search_wait_element),
            'class',                            # атрибут в котором ожидаем
            'button_loading'               # значение атрибута, которое ожидаем, что будет отсутствовать
        )
    )
    result_obj_count = driver.find_element(By.CSS_SELECTOR, elem.search_counter_element).text
    count_from_db = str(search.get_count_of_object_from_db())
    assert result_obj_count == count_from_db, 'Количество объектов не совпадает с данными из БД'