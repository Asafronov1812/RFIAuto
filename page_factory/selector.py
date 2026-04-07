import allure
from selenium.webdriver.common.action_chains import ActionChains
from page_factory.component import Component
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selector(Component):
    @property
    def type_of(self) -> str:
        return 'selector'

    def send_keys(self, value, validate_value=False):
        with allure.step(f'Send keys "{value}" to {self.type_of} "{self.name}"'):
            actions = ActionChains(self.driver)
            actions.move_to_element(self.driver.find_element(*self.locator))
            actions.click()
            actions.send_keys(value)
            actions.perform()

    def should_have_value(self, value: str):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a value "{value}"'):
            locator = self.driver.find_element(*self.locator)
            assert locator.text == value

    def clear(self) -> None:
        with allure.step(f'Clearing {self.type_of} "{self.name}"'):
            self.driver.find_element(*self.locator).clear()

    def wait_for_load(self) -> None:
        with allure.step(f'Waiting for {self.type_of} with name "{self.name}" to load'):
            wait = WebDriverWait(self.driver, 60)
            wait.until(
                EC.text_to_be_present_in_element_attribute(
                    self.locator,
                    'aria-activedescendant',  # атрибут в котором ожидаем
                    'react-select-2-option-0'  # значение атрибута, которое ожидаем, что будет отсутствовать
                )
            )