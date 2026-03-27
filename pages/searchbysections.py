from selenium.webdriver.common.by import By
from pages.mainmenu import MainMenu


class SearchBySections:

    def __init__(self, driver):
        self.driver = driver

    def open(self) :
        main_menu = MainMenu(self.driver)
        main_menu.open()
        main_menu.click_button_select('Поиск по разделам')

    def check_page_is_opened(self):
        page_title = self.driver.find_element(By.CSS_SELECTOR, 'h1[class="header header_h1 type-information-page__header"]').text
        assert page_title == 'Выберите тип имущества для поиска по разделам'

    def click_button_search_section(self, section):
        self.driver.find_element(By.XPATH, '//div[contains(text(), "' + section + '")]/parent::div').click()

    def check_section_count(self):
        sections = self.driver.find_elements(By.CSS_SELECTOR, '[class="type-page-item"]')
        assert len(sections) == 11
