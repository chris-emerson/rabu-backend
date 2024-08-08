from django.test import TestCase
from freezegun import freeze_time
from planner.models import Activity, ItineraryItem

import datetime

FREEZE_TIME = datetime.datetime(2024, 8, 7, 0, 0, 0,
                                tzinfo=datetime.timezone.utc)
TICK_DELTA = datetime.timedelta(seconds=15)
class ItineraryItemTest(TestCase):
    def createItineraryItem(self, description="Test Activity"):
        activity = Activity.objects.create(description=description)

        return ItineraryItem.objects.from_activity(activity)

    @freeze_time(time_to_freeze=FREEZE_TIME)
    def test_created_at_property_equals_initial_datetime(self):
        item = self.createItineraryItem()
        assert item.created_at == FREEZE_TIME

    def test_updated_at_property_increments_on_save(self):
        with freeze_time(FREEZE_TIME) as frozen_datetime:
            item = self.createItineraryItem()
            initial_updated_at = item.updated_at

            frozen_datetime.tick(15)
            item.save()

            assert initial_updated_at == FREEZE_TIME
            assert item.updated_at == (FREEZE_TIME + TICK_DELTA)

    def test_item_has_a_valid_description(self):
        description = "Museum Tour"
        item = self.createItineraryItem(description)
        assert item.__str__() == description
