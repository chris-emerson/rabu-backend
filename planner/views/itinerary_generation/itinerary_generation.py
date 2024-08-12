import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from planner.geolocation import geolocate, extract
from planner.gpt.itinerary_generation.response_mapper import save_response
from planner.serializers import ItinerarySerializer

from planner.tasks import query_gpt

class ItineraryGenerationView(APIView):
    """Endpoint to generate a new Itinerary"""
    allowed_methods = ['POST']
    
    def post(self, request):
        """Create ItineraryGeneration resource"""
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        latitude = body['data']['attributes']['latitude']
        longitude = body['data']['attributes']['longitude']

        geo_data = geolocate.reverse_lookup(latitude, longitude)
        place_name = extract.extract_placename(geo_data)
        

        # Offload the process to background workers so that
        # we can scale the worker pool
        result = query_gpt.s(place_name).delay()

        # Synchronously block thread (v. bad) and return result
        # n.b. In prod Ideally notify client via async websocket / sse
        gpt_response = result.get(timeout=20)

        # Save the Itinerary
        itinerary = save_response(gpt_response, latitude, longitude)

        return Response(ItinerarySerializer(itinerary).data,
                        status=status.HTTP_201_CREATED)
