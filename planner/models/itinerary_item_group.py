from django.db import models
from planner.models.itinerary_item import ItineraryItem
class ItineraryItemGroup(models.Model):
    """ItineraryItemGroup Model
    n.b. This model should not be interacted with directly. Instead,
    all modifications to an Itinerary should go through the root Itinerary
    model.
    """
    label = models.CharField(max_length=255, blank=True)
    items = models.ManyToManyField(
        ItineraryItem,
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.label

