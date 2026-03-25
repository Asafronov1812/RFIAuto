from selenium.webdriver.common.by import By
from pages.homepage import HomePage
import time

def test_home_page_is_open(driver):
    home_page = HomePage(driver)
    home_page.open()
    ind = driver.find_element(By.CSS_SELECTOR, 'div[class="dashboard-card calendar-card"] h3').text
    assert ind == 'Календарь событий'

