__author__ = "Victor Olivares"

import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

class SeleniumScrapper:

    def __init__(self, pivot_url, implicitly_wait=0) -> None:
        self._driver = None
        self._pivot_url = pivot_url
        self._implicitly_wait = implicitly_wait
        self._setup_driver()

    def _setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("window-size=1920,1080")
        #options.add_argument("--start-maximized")

        self._driver = webdriver.Chrome(options=options)
        if self._implicitly_wait > 0:
            self._driver.implicitly_wait(self._implicitly_wait)
        print("Driver setup done.")

    def _wait(self, min_wait: int, max_wait: int=0):
        """
        Return a waiting time when both values are provided 
        return a value beetwen them else min_wait is used
        """
        sleep_time = random.uniform(min_wait, max_wait) if max_wait else min_wait
        time.sleep(sleep_time)

    def get_element_by_xpath(self, xpath):
        """By default this action wait the time specified at _implicitly_wait time"""
        return self._driver.find_element(By.XPATH, xpath)
    
    def get_text_by_xpath(self, xpath):
        text_value = ""
        try:
            text_value = self.get_element_by_xpath(xpath).text
        except:
            print(f'Unable to grab the text from xpath: {xpath}')

        return text_value

    def scroll_and_wait(self, dom_element, delta_x=0, delta_y=0, delay_seconds=1.0):
        """Makes a scroll to the specified element, move and delays the next action"""
        scroll_origin = ScrollOrigin.from_element(dom_element)
        ActionChains(self._driver).scroll_from_origin(scroll_origin, delta_x, delta_y).perform()
        self._wait(delay_seconds)

    def navigate(self):
        """To define the navigation using selenium"""
        pass

    def start(self):
        """Launches the chromedriver"""
        self._driver.get(self._pivot_url)

    def quit(self):
        """Finishes the driver."""
        self._driver.quit()