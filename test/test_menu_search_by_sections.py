from selenium.webdriver.common.by import By
from pages.mainmenu import MainMenu


class MainMenu:
    def __init__(self, driver):
        self.driver = driver

    def open(self) :
        main_menu = MainMenu(self.driver)
        main_menu.open()
        main_menu.click_button_select('Поиск по разделам')

    def click_button_section(self, section):
        self.driver.find_element(By.XPATH, '//div[contains(text(), "' + select + '")]/parent::button').click()menu = MainMenu(self.driver)

