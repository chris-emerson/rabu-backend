from planner.models import ItineraryItem
from planner.serializers.activity import ActivitySerializer
from rest_framework_json_api import (serializers)

class ItineraryItemSerializer(serializers.ModelSerializer):
    """(de-)serialize the ItineraryItem model."""

    activity_data = ActivitySerializer(source='activity',
                                       many=False,
                                       context={'request': None}
                                       )

    included_serializers = {
        'activity': ActivitySerializer,
        'group': 'planner.serializers.ItineraryItemGroupSerializer'
    }
    
    class Meta:
        model = ItineraryItem
        fields = (
            'id',
            'created_at',
            'updated_at',
            'activity',
            'group',
            'activity',
            'activity_data',
            'latitude',
            'longitude'
          )

    class JSONAPIMeta:
        resource_name = "itinerary_item"
        included_resources = ['activity']

