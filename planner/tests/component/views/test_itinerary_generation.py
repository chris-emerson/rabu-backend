"""Component tests for the /itinerary-generation/ endpoint."""
import json
from unittest.mock import patch

import requests_mock
import django.core.serializers.json
from rest_framework.test import APIClient, APIRequestFactory
from django.test import TestCase
from planner.models import Itinerary
from planner.tests.fixtures.geolocading import MAPBOX_SEARCH_RESPONSE, TIMES_SQUARE_ADDRESS, TIMES_SQUARE_LATITDE, TIMES_SQUARE_LOCATION, TIMES_SQUARE_LONGITUDE
from planner.tests.fixtures.googlesearch import GOOGLE_SEARCH_RESPONSE
from planner.tests.fixtures.gpt import build_gpt_itinerary_response
from planner.images import search as image_search_api
from planner.geolocation import geolocate as geolocate_api

class ItineraryGenerationTest(TestCase):

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

        expected_image_search_url = image_search_api.get_url(TIMES_SQUARE_LOCATION)
        expected_reverse_lookup_url = geolocate_api.get_api_url_for_reverse_lookup(
            latitude=TIMES_SQUARE_LATITDE,
            longitude=TIMES_SQUARE_LONGITUDE)
        
        expected_forward_lookup_url = geolocate_api.get_api_url_for_forward_lookup(
            latitude=TIMES_SQUARE_LATITDE,
            longitude=TIMES_SQUARE_LONGITUDE,
            search_text=TIMES_SQUARE_ADDRESS)
        
        expected_gpt_response = build_gpt_itinerary_response(search_text=TIMES_SQUARE_LOCATION,
                                                             full_address=TIMES_SQUARE_ADDRESS)
                
        with requests_mock.Mocker() as m:
            m.register_uri('GET', expected_image_search_url, json=GOOGLE_SEARCH_RESPONSE)
            m.register_uri('GET', expected_reverse_lookup_url, json=MAPBOX_SEARCH_RESPONSE)
            m.register_uri('GET', expected_forward_lookup_url, json=MAPBOX_SEARCH_RESPONSE)

            with patch('celery.result.AsyncResult.get',
                    return_value=expected_gpt_response): 
    
                headers = {
                    "Accept": "application/vnd.api+json",
                    "Access-Control-Allow-Origin": "*" 
                }

                request_body = self.geterate_request_body(
                    TIMES_SQUARE_LATITDE, 
                    TIMES_SQUARE_LONGITUDE)

                response = self.client.post('/itinerary-generation/',
                                            data=request_body,
                                            content_type='application/vnd.api+json',
                                            timeout=20,
                                            **headers)

        self.assertEqual(response.status_code, 201)

        itinerary = Itinerary.objects.last()
        self.assertIsNotNone(itinerary)
        
         
