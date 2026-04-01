import allure
from page_factory.component import Component


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