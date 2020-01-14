from selenium import webdriver
from browser_automation.pages.home_page import HomePage
from browser_automation.pages.portfolio_page import PortfolioPage
from browser_automation.pages.contact_page import ContactPage


browser = webdriver.Chrome()
# Tests for the home page

# Initialize and load the home page
home_pg = HomePage(browser)
home_pg.go()

# Click on the navigation bar and route to the portfolio page
home_pg.click_nav_bar.click()
home_pg.nav_link.click()

# Initialize the portfolio page
portfolio_pg = PortfolioPage(browser)
portfolio_pg.scroll(1919, 1079)
portfolio_pg.scroll(1919, 0)

# Click the "View My CV" button
portfolio_pg.cv_button.click()

# Switch control to the new tab and close it
portfolio_pg.switch(1)
portfolio_pg.close_tab()
portfolio_pg.switch(0)

# Initialize the contact page
contact_pg = ContactPage(browser)
contact_pg.go()

# Fill the contact form and submit
contact_pg.name_input.input_text("Abhishek")
contact_pg.email_input.input_text("abhi_ap@gmail.com")
contact_pg.subject_input.input_text("Automation Test")
contact_pg.message_input.input_text("This is an automated test message")
contact_pg.submit_button.click()

# Quit the browser
browser.quit()
print("Test execution completed successfully!")
