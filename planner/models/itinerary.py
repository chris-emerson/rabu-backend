from django.db import models
from planner.models.itinerary_item import ItineraryItem
from planner.models.itinerary_item_group import ItineraryItemGroup
class ItineraryManager(models.Manager):
    def create_with_new_group(self,
                              itinerary_label="",
                              group_label=""):
        itinerary = Itinerary.objects.create(label=itinerary_label)
        group = ItineraryItemGroup.objects.create(
            label=group_label,
            itinerary=itinerary
        )
        group.save()
        itinerary.save()

        return itinerary

    def create_itinerary_item_for_group(self,
                                        group,
                                        activity):
        itinerary_item = ItineraryItem.objects.create(
            group=group,
            activity=activity)
        itinerary_item.save()

        return self

class Itinerary(models.Model):
    """Itinerary Model

    This model is the root aggregate (DDD) for managing Itineraries.
    External code should interact with this model to manage all
    aspects of Itineraries using the provided methods.

    n.b. ItineraryItemGroup and ItineraryItem models should not be queried
    or referenced directly, since this will make the code harder to maintain
    in the future. See Domain Driven Design by Eric Evans pg125 for details.
    """
    label = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ItineraryManager()

    def __str__(self):
        return self.label

