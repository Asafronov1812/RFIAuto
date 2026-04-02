import pytest
from tests.testdata import search_data


@pytest.mark.smoke
def test_search_by_sections(page_search_by_section) :
    page_search_by_section.open()
    page_search_by_section.check_page_is_opened()
    page_search_by_section.check_section_count(11)

@pytest.mark.smoke
def test_search_by_land(page_search_by_land):
    page_search_by_land.open()
    page_search_by_land.check_page_is_opened()
    page_search_by_land.button_search.click()
    page_search_by_land.button_search.wait_for_load()
    count_from_db = page_search_by_land.get_count_of_object_from_db()
    page_search_by_land.counter.should_have_text(str(count_from_db), 'Количество объектов не совпадает с данными из БД')
