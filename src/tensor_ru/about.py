# from src.base_page import BasePage
from ..base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class TensorAboutSeacrhLocators:
    LOCATOR_TENSOR_WE_WORK_IMAGES = (By.CLASS_NAME, "tensor_ru-About__block3-image")


class TensorAbout(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://tensor.ru/about'

    def get_we_working_images(self):
        return self.find_elements(TensorAboutSeacrhLocators.LOCATOR_TENSOR_WE_WORK_IMAGES, 60000)
