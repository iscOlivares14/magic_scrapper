import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

class SelemiunScrapper():

    SCROLL_DELAY_TIMES = [1,2,3,4,5]

    def __init__(self, pivot_url, implicitly_wait=0) -> None:
        self._driver = None
        self._pivot_url = pivot_url
        self._implicitly_wait = implicitly_wait
        self.init_driver()

    def init_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self._driver = webdriver.Chrome(options=options)
        if self._implicitly_wait > 0:
            self._driver.implicitly_wait(self._implicitly_wait)
        print("Driver initialized...")

    def scroll_and_wait(self, dom_element, delta_x=0, delta_y=0, delay_seconds=None):
        scroll_origin = ScrollOrigin.from_element(dom_element)
        ActionChains(self._driver).scroll_from_origin(scroll_origin, delta_x, delta_y).perform()
        delay_seconds = delay_seconds if delay_seconds else random.choice(self.SCROLL_DELAY_TIMES)
        time.sleep(delay_seconds)    

    def navigate(self):
        """To define the navigation using selenium"""
        pass

    def quit(self):
        self._driver.quit()