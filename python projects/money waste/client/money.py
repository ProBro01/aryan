import datetime

class money:
    wasteCritatria = ['Junk food', 'mall', 'non used things']
    def __init__(self, amount, workName, date, time, meridiem):
        self.amount = amount
        self.workName = workName
        self.date = date
        self.time = time
        self.meridiem = meridiem
        self.waste = None
        self.isWaste()

    def isWaste(self):
        if self.workName in self.wasteCritatria:
            self.waste = True
        else:
            self.waste = False

    def getDate(self):
        return f"{self.date.day}/{self.date.month}/{self.date.year}"
    
    def getTime(self):
        return f"{self.time.hour}:{self.time.minute}:00"
    
    def getMeridiem(self):
        return self.meridiem

    def getName(self):
        return self.workName