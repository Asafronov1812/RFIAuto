from selenium.webdriver.common.by import By
from pages.homepage import HomePage
import time

def test_home_page_is_open(page_home):
    page_home.open()
    page_home.check_page_is_opened()