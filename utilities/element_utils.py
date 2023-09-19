from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElementUtils:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def presence_of_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element

    def presence_of_all_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 40).until(EC.presence_of_all_elements_located(by_locator))
        return elements

    def presence_of_all_element_bool(self, by_locator):
        elements = []
        try:
            elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
            return bool(elements)
        except:
            return bool(elements)
