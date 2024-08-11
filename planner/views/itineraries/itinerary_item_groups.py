from rest_framework_json_api.views import ModelViewSet
from planner.models import ItineraryItemGroup
from planner.serializers import ItineraryItemGroupSerializer
class ItineraryItemGroupsViewSet(ModelViewSet):
    queryset = ItineraryItemGroup.objects.all()
    serializer_class = ItineraryItemGroupSerializer
    allowed_methods = ['GET']

    def get_queryset(self):
        queryset = super().get_queryset()

        # if this viewset is accessed via the 'itineraries-list'
        # route,
        # it wll have been passed the `order_pk` kwarg and the queryset
        # needs to be filtered accordingly; if it was accessed via the
        # unnested '/itineraries' route, the queryset should include all
        # LineItems
        itinerary_pk = self.kwargs.get('itinerary_pk')
        if itinerary_pk is not None:
            queryset = queryset.filter(itinerary_pk=itinerary_pk)

        return queryset