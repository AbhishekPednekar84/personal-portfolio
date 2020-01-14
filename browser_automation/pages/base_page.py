class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def scroll(self, x: int, y: int):
        script = f"window.scrollTo({x}, {y})"
        self.driver.execute_script(script)

    def switch(self, tab: int):
        self.driver.switch_to.window(self.driver.window_handles[tab])

    def close_tab(self):
        self.driver.close()
