"""Example data for mocking ChatGPT responses"""
from .locations import Location

def generate_gpt_itinerary_response(location: Location):
    """Generates an example itinerary response"""
    return  {'itinerary_label': 'Trip to ' + location["name"],
            'itinerary_item_group': 
                [{"label": "Day 1", 
                    "itinerary_items": 
                        [{"activity_description": location["name"], 
                            "activity_full_description": "full description", 
                            "activity_location": {"full_address":location["address"]}}]}]}
