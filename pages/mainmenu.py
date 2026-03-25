from selenium.webdriver.common.by import By
from pages.homepage import HomePage


class MainMenu:
    def __init__(self, driver):
        self.driver = driver

    def open(self) :
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.click_button_main_menu()

    def check_page_is_opened(self, title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, 'h1[class="header header_h1 start-page__header"]').text
        assert page_title == title

    def check_element_count(self, count):
        sections = self.driver.find_elements(By.CSS_SELECTOR, '[class="start-page-item__button-list-item"]')
        assert len(sections) == count