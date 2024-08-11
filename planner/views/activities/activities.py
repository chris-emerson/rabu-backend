from rest_framework_json_api.views import ModelViewSet, RelationshipView
from planner.models import Activity
from planner.serializers import ActivitySerializer

class ActivitiesViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    allowed_methods = ['GET']

