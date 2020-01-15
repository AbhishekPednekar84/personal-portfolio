from browser_automation.pages.base_page import BasePage
from browser_automation.pages.base_element import BaseElement
from selenium.webdriver.common.by import By
from browser_automation.pages.locator import Locator


class ContactPage(BasePage):
    url = "https://www.abhishekpednekar.com/contact"

    @property
    def name_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input#username")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input#email")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def subject_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input#subject")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def message_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value="textarea#message")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def submit_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input#submit")
        return BaseElement(driver=self.driver, locator=locator)
