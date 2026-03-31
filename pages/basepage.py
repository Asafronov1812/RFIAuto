import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver

    def open(self, url: str = 'current_url'):
        with allure.step(f'Opening the url "{url}"'):
            pass

    def visit(self, url: str):
        with allure.step(f'Opening the url "{url}"'):
            self.driver.get(url, wait=WebDriverWait(self.driver, 10))

    def reload(self):
        with allure.step('Reloading the page'):
            self.driver.refresh(wait=WebDriverWait(self.driver, 10))

    def check_page_is_opened(self, title_element, page_title) -> None:
        with allure.step(f'Checking if page is opened for title "{page_title}"'):
            title = self.driver.find_element(By.CSS_SELECTOR, title_element).text
            assert title == page_title, "Не удалось открыть страницу"