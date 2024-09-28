from abc import ABC, abstractmethod
import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

class BaseSelemiunScrapper:

    SCROLL_DELAY_TIMES = [1,2,3,4,5]
    _driver = None

    def init_driver(self, implicitly_wait=None):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self._driver = webdriver.Chrome(options=options)
        if implicitly_wait:
            self._driver.implicitly_wait(implicitly_wait)

    def scroll_and_wait(self, dom_element, delta_x=0, delta_y=0, delay_seconds=None):
        scroll_origin = ScrollOrigin.from_element(dom_element)
        ActionChains(self._driver).scroll_from_origin(scroll_origin, delta_x, delta_y).perform()
        delay_seconds = delay_seconds if delay_seconds else random.choice(self.SCROLL_DELAY_TIMES)
        time.sleep(delay_seconds)    

    def scrape(self):
        pass