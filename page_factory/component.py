from abc import ABC, abstractmethod
import allure


class Component(ABC):
    def __init__(self, driver, locator: tuple, name: str = 'Элемент') -> None:
        self.driver = driver
        self.name = name
        self.locator = locator

    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'component'

    def click(self) -> None:
        with allure.step(f'Clicking {self.type_of} with name "{self.name}"'):
            self.driver.find_element(*self.locator).click()

    def should_be_visible(self) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):
            assert self.driver.find_element(*self.locator).is_displayed()

    def should_be_enabled(self) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" is enabled'):
            assert self.driver.find_element(*self.locator).is_enabled()

    def should_be_clickable(self) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" is clickable'):
            assert self.driver.find_element(*self.locator).is_clickable()

    def should_have_text(self, text) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" is enabled'):
            assert self.driver.find_element(*self.locator).text == text