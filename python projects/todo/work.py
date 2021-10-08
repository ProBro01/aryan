import datetime

class work:
    '''
    a work that has to be done.
    :param name-name of work
    :param time-time at which work has to be done
    :param date-date at which work has to be done
    '''
    def __init__(self, name, hours, minute, year, month, day):
        self.name = name
        time = datetime.time(hours, minute)
        self.time = time
        date = datetime.date(year, month, day)
        self.date = date

    def setName(self, name):
        self.name = name
        return True

    def setTime(self, hours, minute):
        time = datetime.time(hours, minute)
        self.time = time
        return True

    def setDate(self, year, month, day):
        date = datetime.date(year, month, day)
        self.date = date
        return True

    def getName(self):
        return self.name

    def getTime(self):
        return self.time.strftime("%I")+":"+self.time.strftime("%M")+":00"

    def getDate(self):
        return f"{self.date.day}/{self.date.month}/{self.date.year}"
    