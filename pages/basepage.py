import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_factory.button import Button

class BasePage:
    def __init__(self, driver, title_locator: tuple, page_title: str) -> None:
        self.driver = driver
        self.title_locator = title_locator
        self.page_title = page_title
        self.button_main_menu = Button(self.driver, (By.CLASS_NAME, 'main-menu-item__sub-menu-button_active'), 'Кнопка перехода в главное меню')

    def visit(self, url: str):
        with allure.step(f'Opening the url "{url}"'):
            self.driver.get(url, wait=WebDriverWait(self.driver, 10))

    def reload(self):
        with allure.step('Reloading the page'):
            self.driver.refresh(wait=WebDriverWait(self.driver, 10))

    def check_page_is_opened(self) -> None:
        with allure.step(f'Checking if page is opened for title "{self.page_title}"'):
            title = self.driver.find_element(*self.title_locator).text
            assert title == self.page_title, "Не удалось открыть страницу или заголовок не совпадает"