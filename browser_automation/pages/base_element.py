import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(locator=self.locator)
        )
        self.web_element = element

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(locator=self.locator)
        )
        element.click()

    def text(self):
        text = self.web_element.text
        return text

    def input_text(self, text):
        self.web_element.send_keys(text)

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute
