from selenium.webdriver.common.by import By
from pages.searchbysections import SearchBySections


class SearchByLand:

    def __init__(self, driver):
        self.driver = driver

    def open(self) :
        search_by_section = SearchBySections(self.driver)
        search_by_section.open()
        search_by_section.click_button_search_section('1.1. Сведения о земельных участках')

    def check_page_is_opened(self):
        page_title = self.driver.find_element(By.CSS_SELECTOR, 'h1[class="header header_h1 search-filter-block__header"]').text
        assert page_title == 'Поиск разделов 1.1'

    def click_button_search(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="button button_default button_primary search-page__button"]').click()

    def click_button_reset(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="button button_default button_secondary search-page__button-secondary"]').click()