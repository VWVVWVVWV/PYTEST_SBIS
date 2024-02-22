from ..base_page import BasePage
from selenium.webdriver.common.by import By


class SBISSeacrhLocators:
    LOCATOR_SBIS_BUTTON_TENSOR = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor.mb-12")
    LOCATOR_SBIS_BUTTON_REGION_CHOOSER = (By.CSS_SELECTOR,
                                          "#container > div.sbis_ru-content_wrapper.ws-flexbox.ws-flex-column > div > div.sbis_ru-container.sbisru-Contacts__relative > div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > div:nth-child(2) > span > span")
    LOCATOR_SBIS_BLOCK_PARTNERS = (By.CLASS_NAME, "sbisru-Contacts-List__city")
    LOCATOR_SBIS_SEARCH_REGION_FIELD = (By.CSS_SELECTOR, ".controls - Search__nativeField_caretFilled")

    @staticmethod
    def LOCATOR_SBIS_SELECT_REGION_BUTTON(region_code):
        return (By.CSS_SELECTOR,
                f"#popup > div.controls-Popup.ws-float-area-show-complete.controls-Popup_shown.controls_themes__wrapper.controls-Scroll_webkitOverflowScrollingTouch.controls-Popup__lastItem > div > div > div > div > div.sbis_ru-Region-Panel.sbis_ru-Region-Panel-l > div > ul > li:nth-child({region_code}) > span > span")


class SBISContracts(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://sbis.ru/contracts'

    def tensor_click(self):
        self.find_element(SBISSeacrhLocators.LOCATOR_SBIS_BUTTON_TENSOR, 60000).click()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.wait_site()

    def get_region_chooser(self):
        return self.find_element(SBISSeacrhLocators.LOCATOR_SBIS_BUTTON_REGION_CHOOSER, 60000)

    def get_partners(self):
        return self.find_elements(SBISSeacrhLocators.LOCATOR_SBIS_BLOCK_PARTNERS, 60000)

    def get_region_by_code(self, regioncode):
        mainregions = (77, 78)
        if regioncode in range(1, 77):
            number_el = regioncode + 2
        elif regioncode in range(79, 96):
            number_el = regioncode
        elif regioncode in mainregions:
            number_el = mainregions.index(regioncode) + 1
        else:
            raise (f'Undefined region code={regioncode}')
        return self.find_element(SBISSeacrhLocators.LOCATOR_SBIS_SELECT_REGION_BUTTON(str(number_el)), 60000)
