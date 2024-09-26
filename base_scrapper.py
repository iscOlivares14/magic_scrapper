from abc import ABC, abstractmethod
import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

class BaseSelemiunScrapper(ABC):

    def scroll_and_wait(driver, dom_element, delta_x=0, delta_y=0, delay_seconds=None):
        scroll_origin = ScrollOrigin.from_element(dom_element)
        ActionChains(driver).scroll_from_origin(scroll_origin, delta_x, delta_y).perform()
        delay_seconds = delay_seconds if delay_seconds else random.choice(SCROLL_DELAY_TIMES)
        time.sleep(delay_seconds)    

    @abstractmethod
    def scrape(self):
        pass