from django.contrib import admin
from planner.models import Itinerary,ItineraryItem,ItineraryItemGroup,Activity

admin.site.register(Itinerary)
admin.site.register(ItineraryItemGroup)
admin.site.register(ItineraryItem)
admin.site.register(Activity)
