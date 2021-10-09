class Clock:

    def get_position(self, max_hours, mins_passed):
        max_mins = max_hours*60
        position = 0
        for i in range(0, mins_passed):
            if mins_passed == max_mins: position = 0
            position += 1
            i+=1
        return position
