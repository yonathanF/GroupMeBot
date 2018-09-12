from datetime import datetime

from django.test import TestCase

from .models import SimpleUser
from .scheduler import *


class SchedulerAlgoTests(TestCase):
    ''' tests the seheduler '''

    def setUp(self):
        self.today = datetime(2018, 3, 24)
        self.next_week = datetime(2018, 3, 31)
        self.next_year = datetime(2019, 3, 31)

        user1_id = "abc123"
        user1_start = datetime(2018, 3, 19, 10, 20)
        user1_end = datetime(2018, 3, 19, 12, 30)

        user2_id = "abc456"
        user2_start = datetime(2018, 3, 19, 10, 20)
        user2_end = datetime(2018, 3, 19, 13, 30)

        user3 = 'niceid'
        user3_start = datetime(2018, 3, 19, 10, 20)
        user3_end = datetime(2018, 3, 20, 15, 30)

        user2_end_bad = datetime(2018, 3, 19, 10, 30)

        self.user_list = {
            user1_id: [(user1_start, user1_end)],
            user2_id: [(user2_start, user2_end), (user2_start, user2_end_bad)],
            user3: [(user3_start, user3_end), (user2_start, user2_end)]
        }

    def test_create_scheduler_no_injection(self):
        ''' tests creating scheduler without injecting user list '''
        scheduler = Scheduler(self.today, self.next_week, 60)
        self.assertTrue('60' in str(scheduler), "simple test failed")

    def test_create_with_injection(self):
        ''' tests a simple injection into the constructor '''

        scheduler = Scheduler(self.today, self.next_week, 60, self.user_list)
        self.assertTrue('2' in str(scheduler), "simple injection test failed")

    def test_time_difference(self):
        ''' tests the time difference in minuts of a delta '''
        scheduler = Scheduler(self.today, self.next_year, 60)
        diff = self.next_week - self.today

        diff_mins = scheduler.convert_to_minutes(diff)

        self.assertTrue(diff_mins == 10080, "not correctly converting to mins")

    def test_find_overlapp_days(self):
        ''' tests the function that find overlaping days '''

        scheduler = Scheduler(self.today, self.next_year, 60, self.user_list)
        overlapping_days = scheduler.find_overlapping_days()

        #self.assertEqual(expected, overlapping_days, "Overlap days broken")

    def test_find_overlapping_hours(self):
        '''tests the overlapping hour finding function '''

        scheduler = Scheduler(self.today, self.next_year, 60, self.user_list)
        overlapping_days = scheduler.find_overlapping_days()

        day1 = overlapping_days[0][1]

        overlapping_hours = scheduler.find_overlapping_hours(day1)

    def test_perfect_overlap(self):
        ''' tests a list of date with perfect overlaps '''

        scheduler = Scheduler(self.today, self.next_week, 60, self.user_list)
        overlaps = scheduler.find_overlapping("missing_two")
        print(overlaps)
