__author__ = "Victor Olivares"

import argparse
import random
import sys

from bs4 import BeautifulSoup

from base_scrapper import SeleniumScrapper

from utils import download_image

OUTPUT_DIR = "images/output"

class AliScrapper(SeleniumScrapper):
    """
    Goal of this is to get the images located into the description 
    but needs to scroll for reaching that section of the page.
    Then html is parsed using Beautifulsoup.
    """

    # delay times for this scrapper
    SCROLL_DELAY_TIMES = [1,2,3]
    

    def __init__(self, pivot_url, implicitly_wait=0) -> None:
        super().__init__(pivot_url, implicitly_wait)

    def navigate(self) -> None:
        self.start()

        div_product_summary = self.get_element_by_xpath("//div[@class='pdp-info']")
        self.scroll_and_wait(
            div_product_summary, delta_y=600, delay_seconds=random.choice(self.SCROLL_DELAY_TIMES)
        )
        div_product_review = self.get_element_by_xpath("//div[@id='nav-review']")
        self.scroll_and_wait(
            div_product_review, delta_y=600, delay_seconds=random.choice(self.SCROLL_DELAY_TIMES)
        )
        div_product_specs = self.get_element_by_xpath("//div[@id='nav-specification']")
        self.scroll_and_wait(
            div_product_specs, delta_y=600, delay_seconds=random.choice(self.SCROLL_DELAY_TIMES)
        )

        # once all the DOM required is loaded we can close the driver and use only the html
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