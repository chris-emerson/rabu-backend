from django.test import TestCase
from freezegun import freeze_time
from planner.models.activity import Activity

import datetime

FREEZE_TIME = datetime.datetime(2024,8, 7, 0, 0, 0, tzinfo=datetime.timezone.utc)
TICK_DELTA = datetime.timedelta(seconds=15)

class ActivityTest(TestCase):
    @freeze_time(time_to_freeze=FREEZE_TIME)
    def test_created_at_property_equals_initial_datetime(self):
        activity = Activity.objects.create()
        assert activity.created_at == FREEZE_TIME

    def test_updated_at_property_increments_on_save(self):
        with freeze_time(FREEZE_TIME) as frozen_datetime:
            activity = Activity.objects.create()
            initial_updated_at = activity.updated_at

            frozen_datetime.tick(15)
            activity.save()

            assert initial_updated_at == FREEZE_TIME
            assert activity.updated_at == (FREEZE_TIME + TICK_DELTA)

    def test_activity_has_a_valid_description(self):
        description = "Museum Tour"
        item = Activity.objects.create(description=description)
        assert item.__str__() == description
