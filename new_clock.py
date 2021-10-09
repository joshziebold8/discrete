class Clock:

    def get_position(self, max_hours, mins_passed):
        minute_position = mins_passed%60
        hour_position = 0
        for i in range(0, mins_passed/60):
            hour_position+=1
            if max_hours == hour_position: hour_position = 0
            i+=1
        return hour_position, minute_position