class Train:
    def __init__(self,name,*stoppages):
        self.name=name
        self.stoppages=stoppages
        self.passengers=[]
        print(f"Welcome aboard on {self.name}\nStart: {self.stoppages[0]}\nDestination: {self.stoppages[len(self.stoppages)-1]}")
    def addPassenger(self,*passenger):
        for x in passenger:
            if x.start==0 or x.stop==0:
                if x.start==0:
                    x.start=self.stoppages[0]
                if x.stop==0:
                    x.stop=self.stoppages[len(self.stoppages)-1]
            print(f"Welcome aboard {x.name}")
            self.passengers.append(x)
            x.fare=(self.stoppages.index(x.stop)-self.stoppages.index(x.start))*100

    def allPassengerDetails(self):
        for x in self.passengers:
            print(f"Name: {x.name},Start: {x.start},Destination: {x.stop},Fare: ${x.fare}")


class Passenger:
    def __init__(self,name,start=0,stop=0):
        self.name=name
        self.start=start
        self.stop=stop
        self.fare=0
t1 = Train('T1-Express','New York','Manhattan','Brooklyn','Boston')
print("1========================")
p1 =Passenger("Naruto")
t1.addPassenger(p1)
p2 = Passenger("Sasuke","Manhattan")
p3 = Passenger("Hinata","Manhattan","Brooklyn")
print("2========================")
t1.addPassenger(p2,p3)
print("3========================")
t1.allPassengerDetails()
print("4========================")
t2 = Train('Europe-Express','London','Paris','Brussels','Turkey')
print("5========================")
p4 =Passenger("Max","London","Brussels")
p5 = Passenger("Eleven","Paris")
p6 = Passenger("Mike","Brussels")
t2.addPassenger(p4,p5,p6)
print("6========================")
t2.allPassengerDetails()