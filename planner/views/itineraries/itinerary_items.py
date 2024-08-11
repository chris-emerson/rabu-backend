from rest_framework_json_api.views import ModelViewSet, RelationshipView
from planner.models import ItineraryItem
from planner.serializers import ItineraryItemSerializer

class ItineraryItemsViewSet(ModelViewSet):
    queryset = ItineraryItem.objects.all()
    serializer_class = ItineraryItemSerializer
    allowed_methods = ['GET']
