import allure
from selenium.webdriver.common.by import By
from page_factory.button import Button
from pages.basepage import BasePage
from pages.mainmenu import MainMenu
from pages.pagedata import settings


class SearchBySections(BasePage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)

    def open(self) :
        with allure.step(f'Opening the search by sections page'):
            main_menu = MainMenu(self.driver, *settings.page_main_menu_set)
            main_menu.open()
            main_menu.click_button_select('Поиск по разделам')

    def click_button_search_section(self, section) -> None:
        button_locator = (By.XPATH, '//div[contains(text(), "' + section + '")]/parent::div')
        Button(self.driver, button_locator, section).click()

    def check_section_count(self, count: int = 11) -> None:
        with allure.step(f'Checking count of sections, must be equal to {count}'):
            sections = self.driver.find_elements(By.CSS_SELECTOR, '[class="type-page-item"]')
            assert len(sections) == count, "Количество разделов не соответствует ожиданиям"