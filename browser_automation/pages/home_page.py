from browser_automation.pages.base_page import BasePage
from browser_automation.pages.base_element import BaseElement
from selenium.webdriver.common.by import By
from browser_automation.pages.locator import Locator


class HomePage(BasePage):
    url = "https://abhishekpednekar.com"

    @property
    def click_nav_bar(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div.menu-btn")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def nav_link(self):
        locator = Locator(by=By.XPATH, value="//a[text()='Portfolio']")
        return BaseElement(driver=self.driver, locator=locator)
