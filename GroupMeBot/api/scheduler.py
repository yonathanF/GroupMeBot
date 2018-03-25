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
                    current_user = [user, [user_time]]
                    hours_groups[start_in_min] = current_user

                # if there is some data there already
                else:
                    updated = False
                    # try to find the user, it that user is in there already
                    for existing_user in old_time_data:

                        # if the user is here
                        if existing_user[0] == user:
                            # get the current data and append the new time
                            current_data = existing_user[1]
                            current_data.append(user_time)
                            existing_user[1] = current_data

                            # set flag and exist
                            updated = True
                            break

                    # if the user is not in here already
                    if not updated:
                        # create an entry for the user and append it
                        current_user = [user, [user_time]]
                        (hours_groups[start_in_min]).append(current_user)

        for index, hour in enumerate(hours_groups):
            if hour:
                print("-------------[group]" + str(index) + "]---------")
                for user in hour:
                    print(user)
                    print("\n\n")

    def find_overlapping(self):
        ''' a function that tries to find an overlap in the specified list of times '''

        # get the meeting timeframe in minutes
        timeframe_meeting = self.timeframe_end - self.timeframe_start
        total_open_mins = self.convert_to_minutes(timeframe_meeting)

        # find overlaping days
        overlaping_days = self.find_overlapping_days()

        # find overlaping hours

        # partition the time between timeframe start and
        # timeframe end into meeting_length

        return timeframe_meeting

    def schedule(self):
        ''' the entry point into the scheduling algorithm.
        Returns a dictionary as with time/date pair + ranking for that
        meeting block. If there is a tie, it will randmoly pick between the tied
        options and enable a boolean for tied.

        If not common time block is found, it will create blocks such that the
        smallest number of people are missing from the meeting. This will affect the
        ranking, but the format will be the same.
        '''

        raise NotImplementedError()
