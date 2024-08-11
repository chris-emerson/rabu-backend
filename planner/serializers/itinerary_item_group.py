from rest_framework_json_api import (serializers)
from planner.models import ItineraryItemGroup, ItineraryItem
from planner.serializers import ItineraryItemSerializer

class ItineraryItemGroupSerializer(serializers.ModelSerializer):
    """(de-)serialize the ItineraryItemGroup model."""

    itinerary_items = ItineraryItemSerializer(source='itinerary_item_group',
                                              many=True,
                                              context={'request': None})

    included_serializers = {
        'itinerary_items': 'planner.serializers.ItineraryItemGroupSerializer',
    }
    
    def get_itinerary_items(self, instance):
        """Filter the Itinerary Items for this ItineraryItemGroup."""
        return ItineraryItem.objects.filter(group=instance)
    
    class Meta:
        model = ItineraryItemGroup
        fields = (
            'id',
            'label',
            'created_at',
            'updated_at',
            'itinerary',
            'itinerary_items')
        
    class JSONAPIMeta:
        resource_name = "itinerary_item_group",

