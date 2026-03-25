from pages.homepage import HomePage
from pages.mainmenu import MainMenu

def test_main_menu_is_opened(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_button_main_menu()
    main_menu = MainMenu(driver)
    main_menu.check_page_is_opened('Работа с объектами учета')

def test_element_count(driver):
    main_menu = MainMenu(driver)
    main_menu.open()
    main_menu.check_element_count(11)





