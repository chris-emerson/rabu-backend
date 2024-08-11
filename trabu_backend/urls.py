
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework import routers
from planner import views

router = routers.DefaultRouter()
router.register(r'itineraries', views.ItinerariesViewSet)
router.register(r'itinerary_item_groups', views.ItineraryItemGroupsViewSet)
router.register(r'itinerary_items', views.ItineraryItemsViewSet)
router.register(r'activities', views.ActivitiesViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='/v1', permanent=False)),
    path('v1/', include(router.urls)),
    path(r'itinerary-generation/',
        views.ItineraryGenerationView.as_view(),
         name='itinerary-generation'),
    path("admin/", admin.site.urls),
]
