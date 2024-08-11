from django.db import models

class ItineraryItemGroup(models.Model):
    """A django model representing a group of Itinerary Items.
    
    n.b. This model should not be interacted with directly. Instead,
    all modifications to an Itinerary should go through the root Itinerary
    model.
    """
    label = models.CharField(max_length=255, blank=True)
    itinerary = models.ForeignKey(
        'Itinerary',
        related_name='itinerary',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()
    
    def __str__(self):
        return str(self.label)

    class Meta:
        verbose_name = 'Itinerary Item Groups'
        verbose_name_plural = 'Itinerary Item Groups'
