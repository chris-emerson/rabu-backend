from django.test import TestCase
from freezegun import freeze_time

from planner.models import Activity, ItineraryItem
from planner.models.itinerary import Itinerary
from planner.models.itinerary_item_group import ItineraryItemGroup

import datetime

FREEZE_TIME = datetime.datetime(2024,8, 7, 0, 0, 0, tzinfo=datetime.timezone.utc)
TICK_DELTA = datetime.timedelta(seconds=15)
class ItineraryTest(TestCase):

    def test_can_create_itinerary_with_empty_group(self):
        itinerary_label="Test Itinerary"
        group_label="Day 1"
        itinerary = Itinerary.objects.create_with_new_group(
            itinerary_label,
            group_label,
        )
        group = ItineraryItemGroup.objects.filter(itinerary=itinerary).first()
        self.assertEqual(itinerary.__str__(), itinerary_label)
        self.assertEqual(group.__str__(), group_label)

    def test_can_create_itinerary_item_for_group(self):
        itinerary_label="Test Itinerary"
        group_label="Day 1"

        itinerary = Itinerary.objects.create_with_new_group(
            itinerary_label,
            group_label,
        )
        group = ItineraryItemGroup.objects.filter(itinerary=itinerary).first()

        activity = Activity.objects.create(description="Activity One")
        Itinerary.objects.create_itinerary_item_for_group(
            group=group,
            activity=activity
        )
        self.assertEqual(itinerary.__str__(), itinerary_label)
        self.assertEqual(group.__str__(), group_label)

    @freeze_time(time_to_freeze=FREEZE_TIME)
    def test_created_at_property_equals_initial_datetime(self):
        itinerary = Itinerary.objects.create()
        assert itinerary.created_at == FREEZE_TIME

    def test_updated_at_property_increments_on_save(self):
        with freeze_time(FREEZE_TIME) as frozen_datetime:
            itinerary = Itinerary.objects.create_with_new_group(
                itinerary_label="Test Itinerary",
                group_label="Day 1",
            )

            activity = Activity.objects.create(description="Activity One")
            group = ItineraryItemGroup.objects.filter(itinerary=itinerary).first()
            Itinerary.objects.create_itinerary_item_for_group(
                activity=activity,
                group=group
            )

            initial_updated_at = itinerary.updated_at
            frozen_datetime.tick(15)
            itinerary.save()

            self.assertEqual(initial_updated_at, FREEZE_TIME)
            self.assertEqual(itinerary.updated_at, (FREEZE_TIME + TICK_DELTA))
