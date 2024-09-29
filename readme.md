# Scrapping example using selenium and beautifulsoup

This repo uses Selenium and beautifulsoup for getting data
or media content from some pages.

**Note** You should have a [virtualenv](https://virtualenv.pypa.io/en/latest/) where to install the requirements.

```bash
(venv) pip install -r requirements.txt
```

One dependencies are installed you can test the script.For now is specifically focused in one site.
You can get some help using:

```bash
(venv) python3 aliexpress.py -h

# you'll get something like this
usage: aliexpress.py [-h] [-u URL] [-iw IMPLICITLY_WAIT]

Scrapper for images on Ali's product pages

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Ali's URL to start scrape.
  -iw IMPLICITLY_WAIT, --implicitly_wait IMPLICITLY_WAIT
                        Implicitly wait time for selenium driver. Default: 3
```

Then pass the url using the `-u` flag.


```bash
(venv) python3 aliexpress.py -u https://es.aliexpress.com/item/1005006895003798.html?spm=a2g0o.order_list.order_list_main.40.347f194dlOF89p&gatewayAdapt=glo2esp
```

**NOTE** for simplicity the output is saved in `images/output` directory.

## Roadmap

* Replace `print` with `logging` statements.
* Place a containerized version of this.
