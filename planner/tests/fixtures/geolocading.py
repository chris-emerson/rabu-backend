"""Sample data for mocking the gelocation module."""

MAPBOX_SEARCH_RESPONSE = {
        "type": "FeatureCollection",
        "features": [
            {
                "place_name": "Times Square",
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-74.0060, 40.7128] 
            },
            "properties": {
                "name": "Times Square",
                "city": "New York City",
                "address": "7th Ave & Broadway, New York, NY 10036",
                "zip": "10036",
                "coordinates": {"latitude": -74.0060, 
                                    "longitude": 40.7128}
            }
            }
        ]
}