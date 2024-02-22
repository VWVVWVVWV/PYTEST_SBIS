#from src.base_page import BasePage
from ..base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
class SBISSeacrhLocators:
    LOCATOR_SBIS_SEARCH_BUTTON_CONTACTS = (By.CSS_SELECTOR ,"li.sbisru-Header__menu-item:nth-child(2) > a:nth-child(1)")
    LOCATOR_SBIS_SEARCH_FOOTER_ELEMENTS= (By.CLASS_NAME ,"sbisru-Footer__list-item")
class SBISIndexPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://sbis.ru'

    def contacts_click(self):
        return self.find_element(SBISSeacrhLocators.LOCATOR_SBIS_SEARCH_BUTTON_CONTACTS,60000).click()

    def get_footer_elements(self):
        return self.find_elements(SBISSeacrhLocators.LOCATOR_SBIS_SEARCH_FOOTER_ELEMENTS,60000)