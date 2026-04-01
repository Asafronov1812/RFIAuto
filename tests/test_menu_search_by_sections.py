from selenium.webdriver.common.by import By
from pages.searchbysections import SearchBySections
from pages.pagedata import page_elements as elem


def test_search_by_section_is_opened(driver):
    search_by_section = SearchBySections(driver)
    search_by_section.open()
    search_by_section.check_page_is_opened()

def test_button_search_by_section_1_1(driver):
    search_by_section = SearchBySections(driver)
    search_by_section.open()
    search_by_section.click_button_search_section(elem.search_by_land)

