"""This file contains logic to perform a custom google image search."""
import os
import requests

from trabu_backend.settings import GOOGLE_IMAGE_API_KEY, GOOGLE_IMAGE_CX


def lookup_img_url(placeName):
    """Return small photo images relating to a given place."""

    url=(f'https://www.googleapis.com/customsearch/v1?cx={GOOGLE_IMAGE_CX}'
         f'&key={GOOGLE_IMAGE_API_KEY}'
         f'&q={placeName}'
         '&ImgSize=SMALL'
         '&ImgType=photo')

    r = requests.get(url, timeout=20)

    # n.b. Ideally use a JSON query library / JSONPath for production code and handle errors properly
    try:
        img = r.json()["items"][0]['pagemap']['cse_image'][0]['src']
    except:
        img = "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcQXxLOQRv9_WKXHV_HU19USQvFm1VDVVsfccQ8u9ERuOqDMullYMIrAUQcf6NKJdx0nAE2NSrRBqAR6j9sdum5r2TY3Vh3Sw_eJvx-A5A"

    return img