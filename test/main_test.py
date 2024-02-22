import functools
import time
import iuliia
from loguru import logger
from src.sbis_ru import index as sbis_index
from src.sbis_ru import contacts as sbis_contacts
from src.sbis_ru import downloads as sbis_downloads
from src.tensor_ru import index as tensor_index
from src.tensor_ru import about as tensor_about

logger.add('logs/logs_DEBUG.log', level='DEBUG', format="{time} {level} {message}")
logger.add('logs/logs_INFO.log', level='INFO', format="{time} {level} {message}")

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.log('INFO', f"Begin {str(func.__name__)}")
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.log('INFO', f"End {str(func.__name__)} Result - Error")
            logger.log('DEBUG', f"End {str(e)} Result - Error")
            raise (e)
        else:
            logger.log('INFO', f"End {str(func.__name__)} Result - OK")
        return result

    return wrapper


@log_decorator
def test_num1(browser):
    site_page = sbis_index.SBISIndexPage(browser)
    logger.log('INFO', f"Go to page {site_page.base_url}")
    site_page.go_to_site()
    time.sleep(20)
    assert site_page.current_url() == 'https://sbis.ru/'
    logger.log('INFO', f"Go to Contacts over click on button 'Contacts'")
    site_page.contacts_click()
    time.sleep(20)
    assert 'https://sbis.ru/contacts' in site_page.current_url()
    site_page = sbis_contacts.SBISContracts(browser)
    time.sleep(20)
    logger.log('INFO', f"Click on Tensor image and go to Tensor site")
    site_page.tensor_click()
    time.sleep(20)
    site_page = tensor_index.TensorIndex(browser)
    assert site_page.current_url() == 'https://tensor.ru/'
    logger.log('INFO', f"Check block 'Force in People' and click on 'more details' in it block")
    assert site_page.get_force_in_people().text == 'Сила в людях'
    site_page.force_in_people_about_click()
    time.sleep(20)
    assert site_page.current_url() == 'https://tensor.ru/about'
    site_page = tensor_about.TensorAbout(browser)
    logger.log('INFO', f"Check sizes images 'We are working' ")
    images = site_page.get_we_working_images()
    assert len(images) > 0
    width = images[0].get_property('width')
    height = images[0].get_property('height')
    for el in images:
        assert width == el.get_property('width')
        assert height == el.get_property('height')


@log_decorator
def test_num2(browser):
    site_page = sbis_index.SBISIndexPage(browser)
    logger.log('INFO', f"Go to page {site_page.base_url}")
    site_page.go_to_site()
    time.sleep(20)
    assert site_page.current_url() == 'https://sbis.ru/'
    logger.log('INFO', f"Go to Contacts over click on button 'Contacts'")
    site_page.contacts_click()
    time.sleep(20)
    assert 'https://sbis.ru/contacts' in site_page.current_url()
    site_page = sbis_contacts.SBISContracts(browser)
    logger.log('INFO', f"Check current region selected on site is Kaliningradskaya oblast")
    region = site_page.get_region_chooser()
    assert region.text == 'Калининградская обл.'
    logger.log('INFO', f"Check block parners exist")
    partners = site_page.get_partners()
    assert len(partners) > 0
    assert 'Калининград' in [x.text for x in partners]
    logger.log('INFO', f"Click on region button and select 41 region 'Kamchatskiy kray'")
    region.click()
    time.sleep(20)
    setregion = site_page.get_region_by_code(41)
    setregion.click()
    time.sleep(20)
    region = site_page.get_region_chooser()
    logger.log('INFO', f"Check current region selected on site is Kamchatskiy kray")
    assert (iuliia.translate('Камчатский', schema=iuliia.GOST_779_ALT)).lower() in (site_page.current_url()).lower()
    assert 'Камчатский' in site_page.get_title()
    assert region.text == 'Камчатский край'
    assert len(partners) > 1
    assert 'Петропавловск-Камчатский'.lower() in [x.text.lower() for x in partners[:-1]]

@log_decorator
def test_num3(browser):
    site_page = sbis_index.SBISIndexPage(browser)
    logger.log('INFO', f"Go to page {site_page.base_url}")
    site_page.go_to_site()
    time.sleep(20)
    assert site_page.current_url() == 'https://sbis.ru/'
    logger.log('INFO', f"Search button for go to download page ib the footer")
    footerelements = site_page.get_footer_elements()
    assert len(footerelements) > 0
    for el in footerelements:
        if 'Скачать локальные версии' in el.text:
            site_page.go_to_element(el)
            el.click()
            break
    time.sleep(20)
    logger.log('INFO', f"Click on founded download page button and go to download page")
    assert 'https://sbis.ru/download' in site_page.current_url()
    site_page = sbis_downloads.SBISDownloads(browser)
    logger.log('INFO', f"Search button tab of SBIS plugin")
    buttons = site_page.get_sbis_buttons()
    for el in buttons:
        if el.text == 'СБИС Плагин':
            logger.log('INFO', f"Click on founded button tab 'SBIS plugin'")
            site_page.go_to_element(el)
            site_page.script_click(el)
            break
    time.sleep(20)
    logger.log('INFO', f"Search Web installer plugin link and size of file plugin")
    download_link, file_size = site_page.get_download_link('Веб-установщик')
    assert 'https://update.sbis.ru/Sbis3Plugin' in download_link
    assert 'exe' in download_link[-3:]
    assert file_size > 0
    logger.log('INFO', f"Download plugin with control file size")
    filename = site_page.utility.dowmload_contol_size(download_link, file_size)
    assert filename != ''
