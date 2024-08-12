"""Sample data for mocking the gelocation module."""
from .locations import Location

def generate_search_response(location: Location):
    """Returns a mapbox feature collection for the location."""
    return {
        "type": "FeatureCollection",
        "features": [
            {
            "place_name": location["name"],
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [location["latitude"], location["longitude"]] 
            },
            "properties": {
                "name": location["name"],
                "city": "New York City",
                "address": location["address"],
                "zip": "10036",
                "coordinates": {"latitude": location["latitude"], 
                                    "longitude": location["longitude"]}
            }
            }
        ]
}