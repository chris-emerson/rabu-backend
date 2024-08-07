from django.test import TestCase
from freezegun import freeze_time
from planner.models.itinerary import Itinerary

import datetime

FREEZE_TIME = datetime.datetime(2024,8, 7, 0, 0, 0,
                                tzinfo=datetime.timezone.utc)
TICK_DELTA = datetime.timedelta(seconds=15)
class ItineraryTest(TestCase):
    @freeze_time(time_to_freeze=FREEZE_TIME)
    def test_created_at_property_equals_initial_datetime(self):
        itinerary = Itinerary.objects.create()
        assert itinerary.created_at == FREEZE_TIME

    def test_updated_at_property_increments_on_save(self):
        with freeze_time(FREEZE_TIME) as frozen_datetime:
            itinerary = Itinerary.objects.create()
            initial_updated_at = itinerary.updated_at

            frozen_datetime.tick(15)
            itinerary.save()

            assert initial_updated_at == FREEZE_TIME
            assert itinerary.updated_at == (FREEZE_TIME + TICK_DELTA)
