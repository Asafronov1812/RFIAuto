from selenium.webdriver.common.by import By

#page settings for fixtures
page_home_set = ((By.CSS_SELECTOR, 'div[class="dashboard-card calendar-card"] h3'), 'Календарь событий')

page_main_menu_set = ((By.CSS_SELECTOR, 'h1[class="header header_h1 start-page__header"]'), 'Работа с объектами учета')

page_search = ((By.CSS_SELECTOR, 'h1[class="header header_h1 start-page__header"]'), 'Работа с объектами учета')