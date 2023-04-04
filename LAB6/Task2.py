class Assassin:
    counter=0
    def __init__(self,name,success):
        self.name=name
        self.success=success
        Assassin.counter+=1
    @classmethod
    def failureRate(cls,name,failure):
        return cls(name,100-failure)
    @classmethod
    def failurePercentage(cls,name,failure):
        return cls(name,100-int(failure[:-1]))
    def printDetails(self):
        print(f"Name: {self.name}\nSucces rate: {self.success}%\nTotal number of assasin: {Assassin.counter}")
john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()