"""This file contains a Pydantic template for formatting LLM instructions using Langchain.
    This is used to get chat_gpt to return results in a JSON format resembling our domain model,
    and allows for easier maintainence of the prompt. 
"""
from typing import List
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

class GPTActivityLocation(BaseModel):
    """A Pydantic model representing an Activity."""
    full_address: str = Field(description="The name and full address of the itinerary_item activity")
                                    
class GPTItineraryItems(BaseModel):
    """A Pydantic model representing an ItineraryItem."""
    activity_description: str = Field(description="A very concise description of the planned activity")
    activity_full_description: str = Field(description="A long description as to what the activity involves")
    activity_location: GPTActivityLocation

class GPTItineraryItemGroup(BaseModel):
    """A Pydantic model representing an ItineraryGroup."""
    label: str = Field(description="The Day of the planned trip")
    itinerary_items: List[GPTItineraryItems]

class GPTItineraryResponse(BaseModel):
    """A Pydantic model representing an Itinerary."""
    itinerary_label: str = Field(description="Trip to {place_name}")
    itinerary_item_group: List[GPTItineraryItemGroup]

def get_format_instructions():
    """Convert the GPTItineraryResponse model into a format instructions template."""
    pydantic_parser = PydanticOutputParser(pydantic_object=GPTItineraryResponse)
    return pydantic_parser.get_format_instructions()

