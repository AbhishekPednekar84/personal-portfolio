from browser_automation.pages.base_element import BaseElement
from browser_automation.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from browser_automation.pages.locator import Locator


class PortfolioPage(BasePage):

    url = "https://www.abhishekpednekar.com/portfolio"

    @property
    def cv_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value="a.btn-cv")
        return BaseElement(driver=self.driver, locator=locator)
