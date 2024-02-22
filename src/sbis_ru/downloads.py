from ..base_page import BasePage
from selenium.webdriver.common.by import By

class SBISDownloadLocators:
    LOCATOR_SBIS_BUTTON_PLUGIN = (By.CLASS_NAME, "controls-TabButton__caption")
    LOCATOR_SBIS_DOWNLOADS = (By.CLASS_NAME, "sbis_ru-DownloadNew-block.sbis_ru-DownloadNew-flex")
    LOCATOR_SBIS_DOWNLOADS_DESCTIPTION = (By.CLASS_NAME, "sbis_ru-DownloadNew-h3")
    LOCATOR_SBIS_DOWNLOADS_URL = (By.CLASS_NAME, "sbis_ru-DownloadNew-loadLink__link js-link")

class SBISDownloads(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.base_url = 'https://sbis.ru/download'

    @staticmethod
    def str_to_size(strsize):
        posL = strsize.find('(Exe ')
        posR = strsize.find(' МБ)')
        fsize = strsize[posL+5:posR]
        return float(fsize)

    def get_sbis_buttons(self):
        return self.find_elements(SBISDownloadLocators.LOCATOR_SBIS_BUTTON_PLUGIN, 60000)



    def get_download_link(self,download_find_str):
        all_downloads=self.find_elements(SBISDownloadLocators.LOCATOR_SBIS_DOWNLOADS, 60000)
        res_url = ''
        res_size_text = ''

        for el in all_downloads:
            desc=el.find_elements(By.TAG_NAME, 'h3')
            if len(desc)>0:
                if desc[0].text == download_find_str:
                    res_url=el.find_element(By.TAG_NAME,'a').get_property('href')
                    res_size_text=el.find_element(By.TAG_NAME,'a').text
                    break

        return (res_url,self.str_to_size(res_size_text))



