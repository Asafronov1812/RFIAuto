import allure
from selenium.webdriver.common.action_chains import ActionChains
from page_factory.component import Component


class Counter(Component):
    @property
    def type_of(self) -> str:
        return 'counter'