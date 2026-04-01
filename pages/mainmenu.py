import allure
from selenium.webdriver.common.by import By
from pages.pagedata import settings
from page_factory.button import Button
from pages.basepage import BasePage
from pages.homepage import HomePage

class MainMenu(BasePage):

    # main menu
    main_menu_title_element = 'h1[class="header header_h1 start-page__header"]'
    main_menu_title = 'Работа с объектами учета'
    main_menu_sections = (By.CSS_SELECTOR, '[class="start-page-item__button-list-item"]')

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    def open(self) :
        with allure.step(f'Opening the main menu page'):
            home_page = HomePage(self.driver, *settings.page_home_set)
            home_page.open()
            home_page.button_main_menu.click()

    def check_element_count(self, count):
        with allure.step(f'Opening the main menu page'):
            sections = self.driver.find_elements(*self.main_menu_sections)
            assert len(sections) == count

    def click_button_select(self, select):
        button_locator = (By.XPATH, f'//div[contains(text(), "{select}")]/parent::button')
        Button(self.driver, *button_locator, select).click()
        # self.driver.find_element(By.XPATH, '//div[contains(text(), "' + select + '")]/parent::button').click()