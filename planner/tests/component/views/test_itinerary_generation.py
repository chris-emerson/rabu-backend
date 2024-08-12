import json
from rest_framework.test import APIClient, APIRequestFactory
from django.test import TestCase
from planner.models import Itinerary

from unittest.mock import patch

class ItineraryGenerationTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()

    def test_post_request_creates_itinerary(self):
        mock_response = {'itinerary_label': 'Trip to Los Angeles, California',
                         'itinerary_item_group': [{'label': 'Day 1', 'itinerary_items': []},
                                                  {'label': 'Day 2', 'itinerary_items': []},
                                                  {'label': 'Day 3', 'itinerary_items': []}]}


        with patch('celery.result.AsyncResult.get') as mock_get: 
            mock_get.return_value = mock_response

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
