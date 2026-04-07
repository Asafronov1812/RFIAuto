import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from page_factory.component import Component
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Table(Component):

    @property
    def type_of(self) -> str:
        return 'table'

    def hover(self) -> None:
        with allure.step(f'Hovering over {self.type_of} with name "{self.name}"'):
            locator = self.driver.find_element(*self.locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(locator)
            actions.perform()     #возвращает курсор к центру экрана

    def wait_for_load(self) -> None:
        with allure.step(f'Waiting for {self.type_of} with name "{self.name}" to load'):
            wait = WebDriverWait(self.driver, 60)
            wait.until_not(
                EC.text_to_be_present_in_element_attribute(
                    self.locator,
                    'class',  # атрибут в котором ожидаем
                    'table__container_loading'  # значение атрибута, которое ожидаем, что будет отсутствовать
                )
            )

    def click_to_row(self, row: int = 1) -> None:
        with allure.step(f'Clicking on row "{row}" in {self.type_of} with name "{self.name}"'):
            row = (By.XPATH, f'//tbody/tr[{row}]')
            self.driver.find_element(*row).click()

    def select_row(self, row: int = 1) -> None:
        with allure.step(f'Selecting row №"{row}" in {self.type_of} with name "{self.name}"'):
            row = (By.XPATH, f'{self.locator[1]}//tbody/tr[{row}]//div[@class="checkbox documents-tab__checkbox-cell"]')
            self.driver.find_element(*row).click()

    #метод проверяет есть ли объект с тамим параметром в таблице
    def get_row(self, row: int = 1):
        with allure.step(f'Getting info from row №"{row}" of {self.type_of} with name "{self.name}"'):
            row_data = {}
            column_names = self.driver.find_elements(By.XPATH, f'{self.locator[1]}//thead//strong')
            cells = self.driver.find_elements(By.XPATH, f'{self.locator[1]}//tbody//tr[{row}]//td')
            for column_name, cell in zip(column_names, cells):
                row_data[column_name.text] = cell.text
            return row_data

    def checking_row_with_param(self, column_name: str, value: str, row: int = 1) -> None:
        with allure.step(f'Checking that row №{row} of table {self.name} contains {column_name} = {value}'):
            line = self.get_row()
            assert line['Номер запроса'] == value