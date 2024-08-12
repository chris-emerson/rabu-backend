"""Module providing geolocation utilities using the MapBox API."""
import os
import requests
from trabu_backend.settings import MAPBOX_API_TOKEN

def reverse_lookup(latitude, longitude):
    """Search for the nearest place name at a given longitude and latitude.
    
    Keyword arguments:
    latitude -- The latitude
    longitude -- The longitude
    """
    
    url=(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{longitude},{latitude}.'
         f'json?reverseMode=score&types=place&&access_token={MAPBOX_API_TOKEN}')

    r = requests.get(url, timeout=20)
    return r.json()

def forward_lookup(search_text, latitude, longitude):
    """Search for places named x near a location.
    
    Keyword arguments:
    search_text -- The name of the place to lookup.
    latitude -- The latitude to narrow the results by
    longitude -- The longitude to narrow the results by
    """
    url=(f'https://api.mapbox.com/search/geocode/v6/forward?q={search_text}'
         f'&proximity={latitude},{longitude}&access_token={MAPBOX_API_TOKEN}')
    r = requests.get(url, timeout=20)

    return r.json()
