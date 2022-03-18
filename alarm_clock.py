class AlarmClock:
    def __init__(self, time):
        self.current_time = time
        self.alarm_on = True
        self.alarm_set_to = ""

    def set_time(self):
        self.current_time = input("Enter the time:")
        print(f"The current time is now: {self.current_time}")

    def alarm_status(self):
        self.alarm_on = False
        print("Your alarm is now off, enjoy sleeping in!")

    def set_alarm(self):
        self.alarm_set_to = input("What time do you want this alarm to go off at?")
        print(f"This alarm will go off at: {self.alarm_set_to}")

    

    
