#from src.base_page import BasePage
from ..base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
class TensorSeacrhLocators:
    LOCATOR_TENSOR_BLOCK_FORCE_IN_PEOPLE_ABOUT = (By.CSS_SELECTOR, "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a")
    LOCATOR_TENSOR_BLOCK_FORCE_IN_PEOPLE = (By.CSS_SELECTOR, "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p.tensor_ru-Index__card-title.tensor_ru-pb-16")

class TensorIndex(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://tensor.ru/'
    def get_force_in_people(self):
        return self.find_element(TensorSeacrhLocators.LOCATOR_TENSOR_BLOCK_FORCE_IN_PEOPLE,60000)

    def force_in_people_about_click(self):
        element=self.find_element(TensorSeacrhLocators.LOCATOR_TENSOR_BLOCK_FORCE_IN_PEOPLE_ABOUT, 60000)
        self.go_to_element(element)
        time.sleep(60)
        return element.click()

