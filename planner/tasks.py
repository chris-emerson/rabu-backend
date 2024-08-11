from celery import shared_task
from planner.gpt.itinerary_generation.query import query
from planner.gpt.itinerary_generation.response_mapper import save_response

@shared_task
def add(x, y):
    return x + y

@shared_task
def query_gpt(place_name):
    """An async task to query gpt for a holiday"""
    return query(place_name)

@shared_task
def save_gpt_response(gpt_data,latitude,longitude):
    """An async task to save the GPT response to our database."""
    return save_response(gpt_data.get(timeout=1), latitude, longitude)
