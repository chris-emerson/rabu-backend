"""Component tests for the /itinerary-generation/ endpoint."""
import json
from unittest.mock import patch

import requests_mock
from rest_framework.test import APIClient, APIRequestFactory
from django.test import TestCase
from planner.models import Itinerary
from planner.tests.fixtures.geolocading import generate_search_response
from planner.tests.fixtures.googlesearch import GOOGLE_SEARCH_RESPONSE
from planner.tests.fixtures.gpt import generate_gpt_itinerary_response
from planner.images import search as image_search_api
from planner.geolocation import geolocate as geolocate_api
from planner.tests.fixtures.locations import TIMES_SQUARE, Location

class ItineraryGenerationTest(TestCase):
    """Test cases for the Itinerary Generation Resource Endpoint."""

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()

    def geterate_request_body(self, latitute, longitude):
        """Generates a request body for the client"""
        return  json.dumps({
                    "type": "itinerary_generation_views",
                    "data": {
                        "attributes": {
                            "latitude": latitute,
                            "longitude": longitude
                        }
                    }
                })
        
    def test_post_request_creates_itinerary(self):
        search_location: Location = TIMES_SQUARE
        expected_image_search_url = image_search_api.get_url(place_name=search_location["name"])
        expected_reverse_lookup_url = geolocate_api.get_api_url_for_reverse_lookup(
            latitude=search_location["latitude"],
            longitude=search_location["longitude"])
        
        expected_forward_lookup_url = geolocate_api.get_api_url_for_forward_lookup(
            latitude=search_location["latitude"],
            longitude=search_location["longitude"],
            search_text=search_location["address"])
        
        expected_mapbox_response = generate_search_response(search_location)
        expected_gpt_response = generate_gpt_itinerary_response(search_location)
                
        with requests_mock.Mocker() as m:
            m.register_uri('GET', expected_image_search_url, json=GOOGLE_SEARCH_RESPONSE)
            m.register_uri('GET', expected_reverse_lookup_url, json=expected_mapbox_response)
            m.register_uri('GET', expected_forward_lookup_url, json=expected_mapbox_response)

            with patch('celery.result.AsyncResult.get',
                    return_value=expected_gpt_response): 
    
                headers = {
                    "Accept": "application/vnd.api+json",
                    "Access-Control-Allow-Origin": "*" 
                }

                request_body = self.geterate_request_body(
                    search_location["latitude"], 
                    search_location["longitude"])

                response = self.client.post('/itinerary-generation/',
                                            data=request_body,
                                            content_type='application/vnd.api+json',
                                            timeout=20,
                                            **headers)

        self.assertEqual(response.status_code, 201)

        itinerary = Itinerary.objects.last()
        self.assertIsNotNone(itinerary)
        
         
