from selenium.webdriver.common.by import By

#page settings for fixtures
page_home_set = ((By.CSS_SELECTOR, 'div[class="dashboard-card calendar-card"] h3'), 'Календарь событий')
page_main_menu_set = ((By.CSS_SELECTOR, 'h1[class="header header_h1 start-page__header"]'), 'Работа с объектами учета')
page_search_by_sections_set = ((By.CSS_SELECTOR, 'h1[class="header header_h1 type-information-page__header"]'), 'Выберите тип имущества для поиска по разделам')
page_search_by_land_set = ((By.CSS_SELECTOR, 'h1[class="header header_h1 search-filter-block__header"]'), 'Поиск разделов 1.1')