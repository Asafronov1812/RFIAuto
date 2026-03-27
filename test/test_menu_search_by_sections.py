from selenium.webdriver.common.by import By
from pages.searchbysections import SearchBySections


def test_search_by_section_is_opened(driver):
    search_by_section = SearchBySections(driver)
    search_by_section.open()
    search_by_section.check_page_is_opened()

def test_button_search_by_section_1_1(driver):
    search_by_section = SearchBySections(driver)
    search_by_section.open()
    search_by_section.click_button_search_section('1.1. Сведения о земельных участках')

