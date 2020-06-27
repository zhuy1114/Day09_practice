from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver


class Base:
    def __init__(self):
        self.driver = Driver.get_driver()

    def find_elt(self, location, timeout=5, poll_frequency=1):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*location))

    def find_elts(self, location, timeout=5, poll_frequency=1):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*location))

    def click_btn(self, location, timeout=5, poll_frequency=1):
        self.find_elt(location, timeout, poll_frequency).click()

    def send_text(self, location, text, timeout=5, poll_frequency=1):
        input_text = self.find_elt(location, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)


