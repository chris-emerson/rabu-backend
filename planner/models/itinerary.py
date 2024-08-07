from django.db import models
class Itinerary(models.Model):
    """Itinerary Model

    This model is the root aggregate (DDD) for managing Itineraries.
    External code should interact with this model to manage all
    aspects of Itineraries using the provided methods.

    n.b. ItineraryItemGroup and ItineraryItem models should not be queried
    or referenced directly, since this will make the code harder to maintain
    in the future. See Domain Driven Design by Eric Evans pg125 for details.
    """
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

