from django.db import models
class ItineraryItemGroup(models.Model):
    """ItineraryItemGroup Model
    n.b. This model should not be interacted with directly. Instead,
    all modifications to an Itinerary should go through the root Itinerary
    model.
    """
    label = models.CharField(max_length=255, blank=True)
    itinerary = models.ForeignKey(
        'Itinerary',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.label

