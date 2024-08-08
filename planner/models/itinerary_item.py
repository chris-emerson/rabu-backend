from django.db import models
from planner.models.activity import Activity

class ItineraryItemManager(models.Manager):
    def from_activity(self, activity: Activity):
        return self.create(activity=activity)

class ItineraryItem(models.Model):
    """ItineraryItem Model
    n.b. This model should not be interacted with directly. Instead,
    all modifications to an Itinerary should go through the root Itinerary
    model.
    """
    activity = models.ForeignKey(
        Activity,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ItineraryItemManager()

    def __str__(self):
        return self.activity.description

