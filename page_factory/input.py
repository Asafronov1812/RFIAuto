import allure
from page_factory.component import Component
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Input(Component):
    @property
    def type_of(self) -> str:
        return 'input'

    def send_keys(self, value, validate_value=False):
        with allure.step(f'Send keys "{value}" to {self.type_of} "{self.name}"'):
            self.driver.find_element(*self.locator).send_keys(value)
            if validate_value:
                self.should_have_value(value)

    def should_have_value(self, value: str):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a value "{value}"'):
            locator = self.driver.find_element(*self.locator)
            assert locator.text == value

    def clear(self) -> None:
        with allure.step(f'Clearing {self.type_of} "{self.name}"'):
            self.driver.find_element(*self.locator).clear()

    def wait_for_enable(self) -> None:
        with allure.step(f'Waiting for {self.type_of} with name "{self.name}" to be enabled.'):
            wait = WebDriverWait(self.driver, 5)
            wait.until_not(
                EC.text_to_be_present_in_element_attribute(
                    self.locator,
                    'class',  # атрибут в котором ожидаем
                    'react-select--is-disabled'  # значение атрибута, которое ожидаем, что будет отсутствовать
                )
            )