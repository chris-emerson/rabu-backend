from typing import TypedDict

class Location(TypedDict):
    """A dictionary to hold location metadata."""
    name: str
    address: str
    latitude: float
    longitude: float

def get_times_square() -> Location:
    """A Location dict representing Times Square."""
    return {
        "name": "Times Square",
        "address":  "7th Ave & Broadway, New York, NY 10036",
        "latitude": -74.0060,
        "longitude": 40.7128
    }
    
TIMES_SQUARE = get_times_square()
