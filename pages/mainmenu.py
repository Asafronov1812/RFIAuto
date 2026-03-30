from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.homepage import HomePage

class MainMenu(BasePage):

    # main menu
    main_menu_title_element = 'h1[class="header header_h1 start-page__header"]'
    main_menu_title = 'Работа с объектами учета'
    main_menu_sections = '[class="start-page-item__button-list-item"]'

    def __init__(self, driver):
        super().__init__(driver)

    def open(self) :
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.click_button_main_menu()

    def check_page_is_opened(self, title_element = main_menu_title_element, page_title = main_menu_title):
        title = self.driver.find_element(By.CSS_SELECTOR, title_element).text
        assert title == page_title

    def check_element_count(self, count):
        sections = self.driver.find_elements(By.CSS_SELECTOR, self.main_menu_sections)
        assert len(sections) == count

    def click_button_select(self, select):
        self.driver.find_element(By.XPATH, '//div[contains(text(), "' + select + '")]/parent::button').click()