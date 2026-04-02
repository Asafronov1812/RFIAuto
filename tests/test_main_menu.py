import pytest

@pytest.mark.smoke
def test_main_menu(page_mainmenu):
    page_mainmenu.open()
    page_mainmenu.check_page_is_opened()
    page_mainmenu.check_element_count()








