from browser_automation.pages.base_page import BasePage
from browser_automation.pages.base_element import BaseElement
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    url = "https://abhishekpednekar.com"

    @property
    def click_nav_bar(self):
        locator = (By.CSS_SELECTOR, "div.menu-btn")
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def nav_link(self):
        locator = (By.XPATH, "//a[text()='Portfolio']")
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
