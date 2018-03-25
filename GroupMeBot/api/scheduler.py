'''
This module tries to find an optimial meeting time
given a list of constriants:
    1. start of timeframe
    2. end of timeframe
    3. availability of users
        a. open start time
        b. end start time
        c. preferences of user
'''

from datetime import datetime

from .models import SimpleUser


class Scheduler:
    ''' A wrapper for the scheduling algo '''

    def __init__(self,
                 timeframe_start,
                 timeframe_end,
                 meeting_length,
                 users_open_times=None):
        if users_open_times:
            self.users_open_times = users_open_times
        else:
            self.users_open_times = {}

        self.meeting_length = meeting_length
        self.timeframe_start = timeframe_start
        self.timeframe_end = timeframe_end

    def __str__(self):
        return "Meeting Length: " + str(
            self.meeting_length) + "\n Timeframe start: " + str(
                self.timeframe_start) + "\n Timeframe end: " + str(
                    self.timeframe_end) + "\n Number of Users: " + str(
                        len(self.users_open_times))

    def add_user(self, user_open_time):
        ''' Adds a user to be considered in the scheduling process
        user_open_times should be in the format of:
            [user_id, [(open_time1, open_time_end), ...]]

        @note it's a list, not a dictionary!
        '''
        self.users_open_times[user_open_time[0]] = user_open_time[1]

    def remove_user(self, user):
        ''' Removes the user, eg when a prson decides to skip the meeting '''

        del self.users_open_times[user]

    def convert_to_minutes(self, time_difference):
        ''' converts a timedelta into an int mins '''
        days, seconds = time_difference.days, time_difference.seconds

        total_mins = days * 24 * 60
        total_mins += seconds / 60

        return total_mins

    def find_overlapping_days(self):
        ''' a function to find overlap between all the days specified '''

        # day: [count, [[user1, [time1, time2,]], [user2, []], ...]]
        days_of_week = [[0, []] for i in range(7)]

        # get count
        for user in self.users_open_times:
            for open_date in self.users_open_times[user]:
                start_date = open_date[0].date().weekday()
                old_data = days_of_week[start_date]

                # if data exists already, update it, don't overwrite it
                if len(old_data[1]) != 0:
                    old_user_lst = old_data[1]

                    updated = False
                    #check if user already exists
                    for user_days in old_user_lst:
                        if user_days[0] == user:
                            user_days[1].append(open_date)
                            updated = True
                            break

                    if not updated:
                        user_entry = [user, [open_date]]
                        old_user_lst.append(user_entry)

                    update_data = [old_data[0] + 1, old_user_lst]
                    days_of_week[start_date] = update_data

                # if not, just write there
                else:
                    days_of_week[start_date] = [1, [[user, [open_date]]]]

        return days_of_week

    def find_overlapping_hours(self, users):
        ''' takes in a list of users , and finds a list of
        overlapping hours between their days '''

        # break the day into 15 min groups
        # [ [ [user, [(start, end), (start, (end)]], [user, ...] ], [group 2..] ]
        hours_groups = [[] for i in range(360)]

        # find users that have start times within the same 15 min groups
        for user in users:
            for user_time in user[1]:
                start_in_min = user_time[0].time().hour * 15
                old_time_data = hours_groups[start_in_min]

                # if there is data already
                if len(old_time_data) == 0:
                    current_user = [[user[0], [user_time]]]
                    hours_groups[start_in_min] = current_user

                # if there is some data there already
                else:
                    updated = False
                    # try to find the user, it that user is in there already
                    for existing_user in old_time_data:
                        # if the user is here
                        if existing_user[0] == user[0]:
                            # get the current data and append the new time
                            current_data = existing_user[1]
                            current_data.append(user_time)
                            existing_user[1] = current_data
                            # set flag and exist loop
                            updated = True
                            break

                    # if the user is not in here already
                    if not updated:
                        # create an entry for the user and append it
                        current_user = [user[0], [user_time]]
                        hours_groups[start_in_min].append(current_user)

        return hours_groups

    def check_length_of_open_time(self, open_times, meeting_offset):
        ''' takes in a 15 min chunk and checks if those
        who can make the meeting at that time can stay
        for the full length '''

        for time in open_times:
            # check all lengths
            can_attend_full = False
            for time_user in time[1]:
                time_difference = time_user[1] - time_user[0]
                difference_mins = self.convert_to_minutes(time_difference)

                # if the user can stay for that amoung of longer, set flag
                if difference_mins >= self.meeting_length - meeting_offset:
                    can_attend_full = True

            # if none of the times for a give user can enable them
            # to stay long enough, return false
            if not can_attend_full:
                return False

        # everyone can make it otherwise
        return True

    def find_perfect_overlapps(self,
                               overlapping_hours,
                               missing_people=0,
                               meeting_offset=0):
        ''' takes in a list of users and their times
        and picks perfect hours '''

        # get the number of attendees
        number_of_attendees = len(self.users_open_times)

        perfect_overlapps = []
        for day in overlapping_hours:
            for fifteen_min in overlapping_hours[day]:
                # if we have everyone at the start, check if the can make the whole
                # meeting
                if len(fifteen_min) >= (number_of_attendees - missing_people):
                    if self.check_length_of_open_time(fifteen_min,
                                                      meeting_offset):
                        perfect_overlapps.append(fifteen_min)

        return perfect_overlapps

    def merge_closest(self, overlapping_hours, degree=1):
        ''' merges closest two into one block to suggest a meeting date
        that might diverge from the original by up to x  mins '''

        # starts from the top and merges closest two until end
        for day in overlapping_hours:
            for min_chunk in overlapping_hours[day]:
                if min_chunk:
                    raise NotImplementedError("Didn't have time.")

    def generate_report(self, overlap):
        report = "Consider the following options:\n"
        for user in overlap[0]:
            report += "\t" + str(
                (user[1][0][0]).strftime("%c")) + " To " + str(
                    (user[1][0][1]).strftime("%c")) + "\n"

            report += "\n Would you like more options?\n"

            return report

    def find_overlapping(self, overlap_type):
        ''' the entry point into the scheduling algorithm.
        Returns a dictionary as with time/date pair + ranking for that
        meeting block. If there is a tie, it will randmoly pick between the tied
        options and enable a boolean for tied.

        If not common time block is found, it will create blocks such that the
        smallest number of people are missing from the meeting. This will affect the
        ranking, but the format will be the same.
        '''

        # get the meeting timeframe in minutes
        timeframe_meeting = self.timeframe_end - self.timeframe_start

        # find overlaping days
        overlaping_days = self.find_overlapping_days()

        overlapping_hours = {}
        # find overlaping hours
        for index, day in enumerate(overlaping_days):
            if day[0] != 0:
                days_overlapping_hours = self.find_overlapping_hours(day[1])
                overlapping_hours[index] = days_overlapping_hours

        if overlap_type == "perfect":
            # find perfect overlaps
            perfect_overlaps = self.find_perfect_overlapps(overlapping_hours)
            return self.generate_report(perfect_overlaps)

        elif overlap_type == "missing_one":
            # find perfect overlaps with 1 person missing
            missing_one = self.find_perfect_overlapps(overlapping_hours, 1, 1)
            return self.generate_report(missing_one)

        elif overlap_type == "missing_two":
            # find perfect overlaps with 2 people missing
            missing_two = self.find_perfect_overlapps(overlapping_hours, 2)
            return self.generate_report(missing_two)

        elif overlap_type == "15_shorter":
            # find perfect overlaps if the meeting is 15 mins shorter
            shorter_15 = self.find_perfect_overlapps(overlapping_hours, 0, 15)
            return self.generate_report(shorter_15)

        elif overlap_type == "30_shorter":
            # perfect overlaps if meeting is 30 mins shortter
            shorter_30 = self.find_perfect_overlapps(overlapping_hours, 0, 30)
            return self.generate_report(shorter_30)
