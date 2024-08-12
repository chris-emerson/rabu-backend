"""Example data for mocking ChatGPT responses"""

MOCK_GPT_ITINERARY_RESPONSE = {'itinerary_label': 'Trip to Los Angeles, California',
                                'itinerary_item_group': 
                                    [{"label": "Day 1", 
                                        "itinerary_items": 
                                            [{"activity_description": "Times Square", 
                                              "activity_full_description": "full description", 
                                              "activity_location": {"full_address": "7th Ave & Broadway, New York, NY 10036"}}]}]}
            
def build_gpt_itinerary_response(search_text, full_address):
    """Generates an example itinerary response"""
    return  {'itinerary_label': 'Trip to ' + search_text,
                                'itinerary_item_group': 
                                    [{"label": "Day 1", 
                                        "itinerary_items": 
                                            [{"activity_description": search_text, 
                                              "activity_full_description": "full description", 
                                              "activity_location": {"full_address":full_address}}]}]}
            
    