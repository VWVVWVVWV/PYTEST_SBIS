from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import src.utility as utility


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.utility = utility.Utility()

    def find_element(self, locator, time=20):
        el=WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
        return WebDriverWait(self.driver, time).until(EC.visibility_of(el),
                                                      message=f"Can't find element by locator {locator}")
    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self,time=20):
        self.driver.get(self.base_url)
        return self.wait_site(time)
    def wait_site(self,time=20):
        return WebDriverWait(self.driver, time).until_not(EC.new_window_is_opened(self.driver.window_handles[0]))

    def current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def go_to_element(self, element):
        js_code = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js_code, element)

    def script_click(self, element):
        js_code = "arguments[0].click();"
        self.driver.execute_script(js_code, element)
