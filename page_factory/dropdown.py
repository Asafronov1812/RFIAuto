import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from page_factory.component import Component
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DropDown(Component):
    @property
    def type_of(self) -> str:
        return 'dropdown'

    def hover(self) -> None:
        with allure.step(f'Hovering over {self.type_of} with name "{self.name}"'):
            locator = self.driver.find_element(*self.locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(locator)
            actions.perform()     #возвращает курсор к центру экрана

    def click(self, text: str = 'Раздел 1.1 «Сведения о земельных участках»') -> None:
        with allure.step(f'Clicking {self.type_of} element with text "{text}"'):
            locator = self.driver.find_element(By.XPATH, f'//div[contains(@class, "react-select__option") and contains(text(), "{text}")]')
            locator.click()