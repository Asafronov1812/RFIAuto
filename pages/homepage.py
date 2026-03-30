from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class HomePage(BasePage):

    # home page
    URL = 'http://admin.dev.pd15.rosim.mtp/rfi/'
    JWT_URL = 'http://admin.dev.pd15.rosim.mtp/jwt/'
    JWT_element = 'textarea[name="token"]'
    button_main_menu_element = 'main-menu-item__sub-menu-button_active'

    def __init__(self, driver):
        super().__init__(driver)

    def open(self) :
        self.driver.get(self.URL)
        self.driver.find_element(By.ID, 'username').send_keys('rfi_user')
        self.driver.find_element(By.ID, 'password').send_keys('User_5511')
        self.driver.find_element(By.ID, 'kc-login').click()

    def click_button_main_menu(self):
        button_main_menu = self.driver.find_element(By.CLASS_NAME, self.button_main_menu_element)
        button_main_menu.click()

    def get_token(self):
        self.driver.get(self.JWT_URL)
        token = 'Bearer ' + self.driver.find_element(By.CSS_SELECTOR, self.JWT_element).text
        return token