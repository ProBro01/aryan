import money
from datetime import date
import time

class Response:
    def __init__(self):
        self.item_dict = {}
        self.date = date.today()
        self.completeTime = None

    def addMoney(self, money, item):
        '''
        add the money and item to the self.item_dict dictionary 
        '''
        self.item_dict[item] = money

    def removeMoney(self, item):
        """
        remove the money and item to the self.item_dict dictionary 
        """
        self.item_dict.pop(item)

    def getItemDict(self):
        return self.item_dict

    def getDate(self):
        '''
        return the date in regular format
        '''
        return f"{self.date.day}/{self.date.month}/{self.date.year}"

    def getCompleteTime(self):
        '''
        return the time at which the object is completed(mean self.time attribute)
        '''
        return self.completeTime

    def setCompleteTime(self):
        '''
        set self.time when object formation is completed
        '''
        self.completeTime = f"{time.strftime('%X')}"

r = Response()
r.addMoney(10, "patties")
r.addMoney(12, "apple")
r.setCompleteTime()
print(r.getItemDict())
r.removeMoney("apple")
print(r.getItemDict())
print(r.getCompleteTime())