import allure
import pytest
from selenium.webdriver.common.by import By
from page_factory.input import Input
from pages.basepage import BasePage
from page_factory.button import Button


class HomePage(BasePage):

    # home page
    URL = 'http://admin.dev.pd15.rosim.mtp/rfi/'
    JWT_URL = 'http://admin.dev.pd15.rosim.mtp/jwt/'
    JWT_element = 'textarea[name="token"]'

    def __init__(self, driver, title_locator: tuple, page_title: str):
        super().__init__(driver, title_locator, page_title)
        self.input_user_name = Input(self.driver, (By.ID, 'username'), 'Имя пользователя')
        self.input_password = Input(self.driver, (By.ID, 'password'), 'Пароль')
        self.button_enter = Button(self.driver, (By.ID, 'kc-login'), 'Войти')

    def open(self) :
        with allure.step(f'Opening the home page at "{self.URL}"'):
            self.driver.get(self.URL)
            self.input_user_name.send_keys('rfi_user')
            self.input_password.send_keys('User_5511')
            self.button_enter.click()

    def update_token(self):
        with allure.step(f'Updating token in file'):
            self.open()
            self.driver.get(self.JWT_URL)
            token = 'Bearer ' + self.driver.find_element(By.CSS_SELECTOR, self.JWT_element).text
            with open('token.txt', 'w') as file: file.write(token)

    def read_token(self):
        with allure.step(f'Getting token from file'):
            with open("token.txt", "r") as file:
                return file.read()  # Весь текст в одной строке