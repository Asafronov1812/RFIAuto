import allure
from selenium.webdriver.common.action_chains import ActionChains
from page_factory.component import Component
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckBox(Component):
    @property
    def type_of(self) -> str:
        return 'checkbox'

    def hover(self):
        with allure.step(f'Hovering over {self.type_of} with name "{self.name}"'):
            locator = self.driver.find_element(*self.locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(locator)
            actions.perform()    #возвращает курсор к центру экрана
            return actions

    def double_click(self) -> None:
        with allure.step(f'Double clicking {self.type_of} with name "{self.name}"'):
            locator = self.driver.find_element(*self.locator)
            locator.double_click()

    def wait_for_load(self) -> None:
        with allure.step(f'Waiting for {self.type_of} with name "{self.name}" to load'):
            wait = WebDriverWait(self.driver, 60)
            wait.until_not(
                EC.text_to_be_present_in_element_attribute(
                    self.locator,
                    'class',  # атрибут в котором ожидаем
                    'button_loading'  # значение атрибута, которое ожидаем, что будет отсутствовать
                )
            )