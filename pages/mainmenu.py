import allure
from selenium.webdriver.common.by import By
from pages.pagedata import settings
from page_factory.button import Button
from pages.basepage import BasePage
from pages.homepage import HomePage

class MainMenu(BasePage):

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)
        self.button_excerpt_request = Button(self.driver,
                                    (By.CSS_SELECTOR, 'button[class="button button_default button_primary buttons-block-rfi-request-search-page__button"]'),
                                    'Предоставление выписок из РФИ')

    def open(self) :
        with allure.step(f'Opening the main menu page'):
            home_page = HomePage(self.driver, *settings.page_home_set)
            home_page.open()
            home_page.button_main_menu.click()

    def check_element_count(self, count: int = 11) -> None:
        with allure.step(f'Checking count of elements, must be equal to {count}'):
            sections = self.driver.find_elements(By.CSS_SELECTOR, '[class="start-page-item__button-list-item"]')
            assert len(sections) == count

    def click_button_select(self, select):
        button_locator = (By.XPATH, f'//div[contains(text(), "{select}")]/parent::button')
        Button(self.driver, button_locator, select).click()