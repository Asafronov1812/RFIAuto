import allure
from selenium.webdriver.common.action_chains import ActionChains
from page_factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return 'button'

    def hover(self) -> None:
        with allure.step(f'Hovering over {self.type_of} with name "{self.name}"'):
            locator = self.driver.find_element(*self.locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(locator)
            actions.perform()     #возвращает курсор к центру экрана

    def double_click(self) -> None:
        with allure.step(f'Double clicking {self.type_of} with name "{self.name}"'):
            locator = self.driver.find_element(*self.locator)
            locator.double_click()

