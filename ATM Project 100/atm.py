class Atm(object):
    def __init__(self, cardnumber, pinnumber, balance, withdrawal=None):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
        self.balance = balance
        self.withdrawal = withdrawal or {}

    def getBalance(self, cardnumber, pinnumber):
        return self.balance

    def setGrade(self, cardnumber, pinnumber, withdrawal):
        return self.balance - self.withdrawal

john = Atm("John", 12345, 67890, 100000)
jane = Atm("Jane", 67890, 12345, 100000)

print(john.getBalance())
print(jane.getBalance())

print(john.setGrade())
print(jane.setGrade())