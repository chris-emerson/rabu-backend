from django.db import models
from planner.models.itinerary_item_group import ItineraryItemGroup

class ItineraryItem(models.Model):
    """A django module representing a single Itinerary Item.
    
    n.b. This model should not be interacted with directly. Instead,
    all modifications to an Itinerary should go through the root Itinerary
    model.
    """
    activity = models.ForeignKey(
        'Activity',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name="itinerary_item"
    )
    group = models.ForeignKey(
        ItineraryItemGroup,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name="itinerary_item_group"
    )
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
        
    def __str__(self):
        return str(self.activity.description)

    class Meta:
        verbose_name = 'Itinerary Item'
        verbose_name_plural = 'Itinerary Items'

