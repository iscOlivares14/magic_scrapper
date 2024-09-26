import random
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from utils import download_image

# item_url = 'https://es.aliexpress.com/item/1005006376464306.html?spm=a2g0o.order_list.order_list_main.4.347f194dP7bqst&gatewayAdapt=glo2esp'
item_url = 'https://es.aliexpress.com/item/1005006895003798.html?spm=a2g0o.order_list.order_list_main.40.347f194dlOF89p&gatewayAdapt=glo2esp'

SCROLL_DELAY_TIMES = [1,2,3,4,5]
OUTPUT_DIR = "images/output"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)
driver.get(item_url)

def scroll_and_wait(driver, dom_element, delta_x=0, delta_y=0, delay_seconds=None):
    scroll_origin = ScrollOrigin.from_element(dom_element)
    ActionChains(driver).scroll_from_origin(scroll_origin, delta_x, delta_y).perform()
    delay_seconds = delay_seconds if delay_seconds else random.choice(SCROLL_DELAY_TIMES)
    time.sleep(delay_seconds)    

# take advantage of the implicit wait to pass the page fully_loaded to make the soup
div_product_summary = driver.find_element(By.CSS_SELECTOR, "div.pdp-info")
scroll_and_wait(driver, div_product_summary, delta_y=600)
# scroll_origin = ScrollOrigin.from_element(div_product_summary)
# ActionChains(driver).scroll_from_origin(scroll_origin, 0, 600).perform()
# time.sleep(random.choice(SCROLL_DELAY_TIMES))
div_product_review = driver.find_element(By.CSS_SELECTOR, "div#nav-review")
scroll_and_wait(driver, div_product_review, delta_y=600)
# scroll_origin = ScrollOrigin.from_element(div_product_review)
# ActionChains(driver).scroll_from_origin(scroll_origin, 0, 600).perform()
# time.sleep(random.choice(SCROLL_DELAY_TIMES))
div_product_specs = driver.find_element(By.CSS_SELECTOR, "div#nav-specification")
scroll_and_wait(driver, div_product_specs, delta_y=600)
# scroll_origin = ScrollOrigin.from_element(div_product_specs)
# ActionChains(driver).scroll_from_origin(scroll_origin, 0, 600).perform()
# time.sleep(random.choice(SCROLL_DELAY_TIMES))

soup = BeautifulSoup(driver.page_source, 'lxml')

driver.quit()

div_description = soup.find_all('div', {'id': 'product-description'})
if div_description:
    print("looking for product images from description...")
    img_product_list = div_description[0].find_all('img')
    for img in img_product_list:
        print(f"Request for {img['src']}")
        downloaded = download_image(OUTPUT_DIR, img['src'])
        if downloaded:
            print('Image successfully created.')
else:
    print("div#product-description element not found ")