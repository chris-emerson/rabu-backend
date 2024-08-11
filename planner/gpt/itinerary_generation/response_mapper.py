"""This file contains logic to Create a new Itinerary from a GPT response."""
from planner.geolocation.geolocate import forward_lookup, extract_coordinates
from planner.images.search import lookup_img_url
from planner.models import Activity, Itinerary, ItineraryItem, ItineraryItemGroup

def save_response(gpt_response, latitude, longitude):
    """Save a Chat GPT response to an Itinerary.
    
    Keyword arguments:
    gpt_response -- A response from chat gpt formatted in our response template.
    latitude -- The lattiude of our search location.
    longitude -- The longitude of our search location.
    """
    itinerary = Itinerary.objects.create(label=gpt_response["itinerary_label"])
    for group_data in gpt_response["itinerary_item_group"]:
        group = ItineraryItemGroup.objects.create(
            label=group_data["label"],
            itinerary=itinerary
        )
        for item in group_data["itinerary_items"]:
            search_address = item["activity_location"]["full_address"]

            location_features = forward_lookup(search_address, latitude, longitude)
            coordinates = extract_coordinates(location_features)
            img_url = lookup_img_url(item["activity_description"])

            activity = Activity.objects.create(description=item["activity_description"],
                                               full_description=item["activity_full_description"],
                                               image=img_url)
            ItineraryItem.objects.create(
                activity=activity,
                group=group,
                longitude=coordinates["longitude"],
                latitude=coordinates["latitude"],
            )
    itinerary.save()

    return itinerary