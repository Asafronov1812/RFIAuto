import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self) :
        self.driver.get('http://admin.dev.pd15.rosim.mtp/rfi/')
        self.driver.find_element(By.ID, 'username').send_keys('rfi_user')
        self.driver.find_element(By.ID, 'password').send_keys('User_5511')
        self.driver.find_element(By.ID, 'kc-login').click()

    def click_button_main_menu(self):
        button_main_menu = self.driver.find_element(By.CLASS_NAME, 'main-menu-item__sub-menu-button_active')
        button_main_menu.click()