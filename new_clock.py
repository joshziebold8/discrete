class Clock:

    def get_position(self, max_hours, mins_passed):
        max_mins = max_hours*60
        minute_position = 0
        hour_position = 0
        for i in range(0, mins_passed):
            if mins_passed == max_mins: minute_position = 0
            if mins_passed/60 == max_hours: hour_position = 0
            if mins_passed%60 == 0: hour_position+=1
            minute_position += 1
            i+=1
        return hour_position, minute_position
