from browser_automation.pages.base_element import BaseElement
from browser_automation.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PortfolioPage(BasePage):

    url = "https://www.abhishekpednekar.com/portfolio"

    @property
    def cv_button(self):
        locator = (By.CSS_SELECTOR, "a.btn-cv")
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
