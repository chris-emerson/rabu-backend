"""Component tests for the /itinerary-generation/ endpoint."""
import json
from unittest.mock import patch
from rest_framework.test import APIClient, APIRequestFactory
from django.test import TestCase
from planner.models import Itinerary
from planner.tests.fixtures.geolocading import MAPBOX_SEARCH_RESPONSE
from planner.tests.fixtures.googlesearch import GOOGLE_SEARCH_RESPONSE
from planner.tests.fixtures.gpt import MOCK_GPT_ITINERARY_RESPONSE

class ItineraryGenerationTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()

    def test_post_request_creates_itinerary(self):

        with patch('celery.result.AsyncResult.get',
                   return_value=MOCK_GPT_ITINERARY_RESPONSE): 
            with patch('planner.geolocation.geolocate.reverse_lookup',
                       return_value=MAPBOX_SEARCH_RESPONSE):
                with patch('planner.geolocation.geolocate.forward_lookup',
                           return_value=MAPBOX_SEARCH_RESPONSE):
                    with patch('planner.images.search.get_features', 
                               return_value=GOOGLE_SEARCH_RESPONSE):
                        headers = {
                            "Accept": "application/vnd.api+json",
                            "Access-Control-Allow-Origin": "*" 
                        }

                        data = {
                            "type": "itinerary_generation_views",
                            "data": {
                                "attributes": {
                                    "latitude": 34.0522,
                                    "longitude": -118.2437
                                }
                            }
                        }

                        response = self.client.post('/itinerary-generation/',
                                                    data=json.dumps(data),
                                                    content_type='application/vnd.api+json',
                                                    timeout=20,
                                                    **headers)

        self.assertEqual(response.status_code, 201)

        itinerary = Itinerary.objects.last()
        self.assertIsNotNone(itinerary)
