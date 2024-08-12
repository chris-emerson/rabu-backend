"""Module providing geolocation utilities using the MapBox API."""
import os
import requests
import urllib.parse

from trabu_backend.settings import MAPBOX_API_TOKEN

def get_api_url_for_reverse_lookup(longitude, latitude):
    """Generates a url for performing a reverse lookup search"""
    return (f'https://api.mapbox.com/geocoding/v5/mapbox.places/{longitude},{latitude}.'
            f'json?reverseMode=score&types=place&&access_token={MAPBOX_API_TOKEN}')

def get_api_url_for_forward_lookup(longitude, latitude, search_text):
    """Generates a url for performing a forward lookup search"""
    return (f'https://api.mapbox.com/search/geocode/v6/forward?q={urllib.parse.quote(search_text)}'
         f'&proximity={latitude},{longitude}&access_token={MAPBOX_API_TOKEN}')
    
def reverse_lookup(latitude, longitude):
    """Search for the nearest place name at a given longitude and latitude.
    
    Keyword arguments:
    latitude -- The latitude
    longitude -- The longitude
    """
    
    url=get_api_url_for_reverse_lookup(latitude=latitude,longitude=longitude)

    r = requests.get(url, timeout=20)
    return r.json()

def forward_lookup(search_text, latitude, longitude):
    """Search for places named x near a location.
    
    Keyword arguments:
    search_text -- The name of the place to lookup.
    latitude -- The latitude to narrow the results by
    longitude -- The longitude to narrow the results by
    """
    url = get_api_url_for_forward_lookup(longitude=longitude, 
                                            latitude=latitude, 
                                            search_text=search_text)
    r = requests.get(url, timeout=20)

    return r.json()
