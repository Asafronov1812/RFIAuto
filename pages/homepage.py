from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class HomePage(BasePage):

    # home page
    URL = 'http://admin.dev.pd15.rosim.mtp/rfi/'
    JWT_URL = 'http://admin.dev.pd15.rosim.mtp/jwt/'
    JWT_element = 'textarea[name="token"]'
    button_main_menu_element = 'main-menu-item__sub-menu-button_active'
    title = 'Календарь событий'
    title_element = 'div[class="dashboard-card calendar-card"] h3'

    def __init__(self, driver):
        super().__init__(driver)

    def open(self) :
        self.driver.get(self.URL)
        self.driver.find_element(By.ID, 'username').send_keys('rfi_user')
        self.driver.find_element(By.ID, 'password').send_keys('User_5511')
        self.driver.find_element(By.ID, 'kc-login').click()

    def check_page_is_opened(self, element = title_element, page_title = title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, element).text
        assert page_title == self.title, 'Не удалось открыть страницу'

    def click_button_main_menu(self):
        button_main_menu = self.driver.find_element(By.CLASS_NAME, self.button_main_menu_element)
        button_main_menu.click()

    def update_token(self):
        self.open()
        self.driver.get(self.JWT_URL)
        token = 'Bearer ' + self.driver.find_element(By.CSS_SELECTOR, self.JWT_element).text
        with open('token.txt', 'w') as file: file.write(token)

    def read_token(self):
        with open("token.txt", "r") as file:
            return file.read()  # Весь текст в одной строке