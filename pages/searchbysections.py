from selenium.webdriver.common.by import By
from pages.mainmenu import MainMenu

class SearchBySections:

    # search by sections
    search_by_sections_title_element = 'h1[class="header header_h1 type-information-page__header"]'
    search_by_sections_title = 'Выберите тип имущества для поиска по разделам'
    search_by_sections_sections = '[class="type-page-item"]'
    search_by_land = '1.1. Сведения о земельных участках'

    def __init__(self, driver):
        self.driver = driver

    def open(self) :
        main_menu = MainMenu(self.driver)
        main_menu.open()
        main_menu.click_button_select('Поиск по разделам')

    def check_page_is_opened(self, title_element = search_by_sections_title_element, page_title = search_by_sections_title):
        title = self.driver.find_element(By.CSS_SELECTOR, title_element).text
        assert title == page_title

    def click_button_search_section(self, section):
        self.driver.find_element(By.XPATH, '//div[contains(text(), "' + section + '")]/parent::div').click()

    def check_section_count(self, count):
        sections = self.driver.find_elements(By.CSS_SELECTOR, self.search_by_sections_sections)
        assert len(sections) == count
