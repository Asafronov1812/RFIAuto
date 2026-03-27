from pages.mainmenu import MainMenu
from pages.searchbysections import SearchBySections

def test_main_menu_is_opened(driver):
    main_menu = MainMenu(driver)
    main_menu.open()
    main_menu.check_page_is_opened()

def test_element_count(driver):
    main_menu = MainMenu(driver)
    main_menu.open()
    main_menu.check_element_count(11)

def test_button_search_by_section(driver):
    main_menu = MainMenu(driver)
    main_menu.open()
    main_menu.click_button_select('Поиск по разделам')
    SearchBySections(driver).check_page_is_opened()








