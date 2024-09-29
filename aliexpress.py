import argparse
import sys

from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By

from base_scrapper import SelemiunScrapper

from utils import download_image

# item_url = 'https://es.aliexpress.com/item/1005006376464306.html?spm=a2g0o.order_list.order_list_main.4.347f194dP7bqst&gatewayAdapt=glo2esp'
item_url = 'https://es.aliexpress.com/item/1005006895003798.html?spm=a2g0o.order_list.order_list_main.40.347f194dlOF89p&gatewayAdapt=glo2esp'
# item_url = "https://es.aliexpress.com/item/1005007221056183.html?spm=a2g0o.detail.pcDetailBottomMoreOtherSeller.3.4113v1VRv1VRXP&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.40050.354490.0&scm_id=1007.40050.354490.0&scm-url=1007.40050.354490.0&pvid=e686259c-ca2c-4369-a265-5a60ef4cbcb8&_t=gps-id:pcDetailBottomMoreOtherSeller,scm-url:1007.40050.354490.0,pvid:e686259c-ca2c-4369-a265-5a60ef4cbcb8,tpp_buckets:668%232846%238116%232002&pdp_npi=4%40dis%21MXN%21536.28%21413.02%21%21%2126.80%2120.64%21%40210318c317273708776387970e68b7%2112000039859310573%21rec%21MX%213220716497%21X&utparam-url=scene%3ApcDetailBottomMoreOtherSeller%7Cquery_from%3A"

OUTPUT_DIR = "images/output"

class AliScrapper(SelemiunScrapper):
    """
    Goal of this is to get the images located into the description 
    but needs to scroll for reaching that section of the page.
    Then html is parsed using Beautifulsoup.
    """

    def __init__(self, pivot_url, implicitly_wait=0) -> None:
        super().__init__(pivot_url, implicitly_wait)

    def navigate(self) -> None:
        print("initialized")
        self._driver.get(item_url)

        # take advantage of the implicit wait to pass the page fully_loaded to make the soup
        div_product_summary = self._driver.find_element(By.CSS_SELECTOR, "div.pdp-info")
        self.scroll_and_wait(div_product_summary, delta_y=600)
        div_product_review = self._driver.find_element(By.CSS_SELECTOR, "div#nav-review")
        self.scroll_and_wait(div_product_review, delta_y=600)
        div_product_specs = self._driver.find_element(By.CSS_SELECTOR, "div#nav-specification")
        self.scroll_and_wait(div_product_specs, delta_y=600)

        soup = BeautifulSoup(self._driver.page_source, 'lxml')

        self.quit()

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Scrapper for images on Ali's product pages")
    parser.add_argument('-u', '--url',type=str, help='Ali\'s URL to start scrape.')
    parser.add_argument('-iw', '--implicitly_wait', default=3, type=int,
                       help='Implicitly wait time for selenium driver. Default: %(default)s')
    args = parser.parse_args()
    
    if not args.url:
        print("URL is required to scrape")
        raise SystemExit(1)
    
    ali = AliScrapper(args.url, args.implicitly_wait)
    ali.navigate()