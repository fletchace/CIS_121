class Time:
    def __init__(self, hours, minutes):
        self.hours = int(hours)
        self.minutes = int(minutes)
    def __add__(self, other_time):
        hour = self.hours + other_time.hours
        minute = self.minutes + other_time.minutes
        if minute >= 60:
            minute -= 60
            hour += 1
        return f"{hour} hours {minute} minutes"
    def __str__(self):
        return f"{self.hours}h {self.minutes}m"

time1 = Time(1,30)
time2 = Time(2,45)

print(time1 + time2)