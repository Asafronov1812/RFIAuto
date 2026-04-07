import allure
from selenium.webdriver.common.action_chains import ActionChains
from page_factory.component import Component
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DatePicker(Component):
    @property
    def type_of(self) -> str:
        return 'datepicker'

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