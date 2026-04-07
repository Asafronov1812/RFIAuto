import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from page_factory.component import Component
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page(Component):
    @property
    def type_of(self) -> str:
        return 'page'

    def wait_for_load(self) -> None:
        with allure.step(f'Waiting for {self.type_of} with name "{self.name}" to load'):
            wait = WebDriverWait(self.driver, 60)
            locator = (By.CSS_SELECTOR, 'div[class="loader-container"]')
            wait.until_not(EC.presence_of_element_located(locator))