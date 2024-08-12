from celery import shared_task
from planner.gpt.itinerary_generation.query import query

@shared_task
def add(x, y):
    return x + y

@shared_task
def query_gpt(place_name):
    """An async task to query gpt for a holiday"""
    return query(place_name)