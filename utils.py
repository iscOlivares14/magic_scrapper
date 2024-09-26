import os
from io import BytesIO

from PIL import Image
import requests


def get_name_from_url(url):
    url_base, _ = url.split('?') if url.count('?') else (url, None)
    image_name = url_base.split('/')[-1]
    return os.path.splitext(image_name)

def download_image(outputdir, url):
    name, extension = get_name_from_url(url)
    extension = '.jpeg' if extension == '.jpg' else extension
    r = requests.get(url)
    downloaded = False

    if r.status_code == requests.codes.ok:
        try:
            new_image = Image.open(BytesIO(r.content))
            outfile = os.path.join(outputdir, f'{name}{extension}')
            new_image.save(outfile)
            downloaded = True
        except OSError:
            print("Failed creating the image")
    
    return downloaded
