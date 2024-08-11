from rest_framework_json_api.views import ModelViewSet, RelationshipView
from planner.models import Itinerary
from planner.serializers import ItinerarySerializer

class ItinerariesViewSet(ModelViewSet):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    allowed_methods = ['GET']
