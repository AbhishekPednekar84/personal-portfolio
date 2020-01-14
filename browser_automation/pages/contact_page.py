from browser_automation.pages.base_page import BasePage
from browser_automation.pages.base_element import BaseElement
from selenium.webdriver.common.by import By


class ContactPage(BasePage):
    url = "https://www.abhishekpednekar.com/contact"

    @property
    def name_input(self):
        locator = (By.CSS_SELECTOR, "input#username")
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def email_input(self):
        locator = (By.CSS_SELECTOR, "input#email")
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def subject_input(self):
        locator = (By.CSS_SELECTOR, "input#subject")
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def message_input(self):
        locator = (By.CSS_SELECTOR, "textarea#message")
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def submit_button(self):
        locator = (By.CSS_SELECTOR, "input#submit")
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
