from planner.models import Itinerary
from planner.serializers import ItineraryItemGroupSerializer
from rest_framework_json_api import (serializers)

class ItinerarySerializer(serializers.ModelSerializer):
    """(de-)serialize the Itinerary model."""

    serializer_context = {'request': None}
    itinerary_item_groups = ItineraryItemGroupSerializer(
        source='itinerary',
        many=True,
        context={'request': None})

    class Meta:
        model = Itinerary
        fields = (
            'id',
            'label',
            'created_at',
            'updated_at',
            'itinerary_item_groups')

    class JSONAPIMeta:
        resource_name = "itinerary"
