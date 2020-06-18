class Clock:
   def __init__(self, hour, minute):  
        all_time=hour*60+minute
        self.hour = (all_time//60)%24
        self.minute =all_time % 60

   def __repr__(self):
        #return f"{self.hour:02}:{self.minute:02}"
        return "%02d:%02d"%(self.hour,self.minute)
   def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

   def __add__(self, minutes):
        
        return Clock(self.hour, self.minute+minutes)

   def __sub__(self, minutes):
        
        return Clock(self.hour, self.minute-minutes)