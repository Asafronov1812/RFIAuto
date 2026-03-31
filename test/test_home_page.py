from selenium.webdriver.common.by import By
from pages.homepage import HomePage
import time

def test_home_page_is_open(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.check_page_is_opened()