from rest_framework_json_api import (serializers)
from planner.models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    """(de-)serialize the Activity model."""
    
    class Meta:
        model = Activity
        fields = (
            'id',
            'description',
            'created_at',
            'updated_at',
            'itinerary_item',
            'image',
        'full_description')

    class JSONAPIMeta:
        resource_name = "activity",
        included_fields = ['description']
