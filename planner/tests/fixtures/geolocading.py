"""Sample data for mocking the gelocation module."""
TIMES_SQUARE_LOCATION = "Times Square"
TIMES_SQUARE_ADDRESS = "7th Ave & Broadway, New York, NY 10036"
TIMES_SQUARE_LATITDE = -74.0060
TIMES_SQUARE_LONGITUDE = 40.7128

MAPBOX_SEARCH_RESPONSE = {
        "type": "FeatureCollection",
        "features": [
            {
            "place_name": TIMES_SQUARE_LOCATION,
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [TIMES_SQUARE_LATITDE, TIMES_SQUARE_LONGITUDE] 
            },
            "properties": {
                "name": TIMES_SQUARE_LOCATION,
                "city": "New York City",
                "address": TIMES_SQUARE_ADDRESS,
                "zip": "10036",
                "coordinates": {"latitude": TIMES_SQUARE_LATITDE, 
                                    "longitude": TIMES_SQUARE_LONGITUDE}
            }
            }
        ]
}