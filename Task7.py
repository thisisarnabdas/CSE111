class BracuBus:
  def __init__(self,dst,cap=2):
    self.dst=dst
    self.cap=cap
    self.pcount=0
    self.plist=[]
  def show_details(self):
    print(f"Bus Route: {self.dst}")
    print(f"Passengers Count: {self.pcount} (Max:{self.cap})")
    print(f"Passengers On Board : {self.plist}")
  def board(self,*nop):
    if len(nop)==0:
      print("No passenger!")
    else:
      for i in nop:
        if i.home==self.dst and i.bpass==True and self.pcount<self.cap:
          print(f"{i.name} boarded the bus")
          self.plist.append(i.name)
          if self.pcount>=self.cap:
            print("Bus is full!")
          self.pcount+=1
        elif i.home!=self.dst or i.bpass==False:
          if i.home!=self.dst:
            print("You got on wrong bus!")
          elif i.bpass==False:
            print("You don't have bus pass!")
        elif self.pcount>=self.cap:
          print("Bus is full!")
class BracuStudent:
  def __init__(self,name,loc):
    self.name=name
    self.home=loc
    self.bpass=False
  def show_details(self):
      print(f"Student Name : {self.name}")
      print(f"Lives in {self.home}")
      print(f"Have Bus Pass? {self.bpass}")
  def get_pass(self):
     self.bpass=True

st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()