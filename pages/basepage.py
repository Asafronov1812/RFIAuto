from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        pass

    def check_page_is_opened(self, title_element, page_title):
        title = self.driver.find_element(By.CSS_SELECTOR, title_element).text
        assert title == page_title