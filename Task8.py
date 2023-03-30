class Library:
    def __init__(self,name,books):
        self.name=name
        self.books=books
        self.borrower={}
    def details(self):
        print(f"{self.name} Library details")
        print(f"Borrower details: ")
        print(self.borrower)
        print(f"Books availability:")
        print(self.books)
class Reader:
    def __init__(self,name):
        self.name=name
        self.books={}
    def borrow(self,library,*books):
        for x in books:
            if sum(self.books.values())<5 and library.books[x]>=0:
                    if library.books[x]==0:
                        print(f"{x} books are not available at the moment.")
                    elif library.books[x]>0:
                        print(f"{x} book is borrowed successfully.")
                        library.books[x]-=1
                        if x not in self.books:
                            self.books[x]=1
                        else:
                            self.books[x]+=1
            elif sum(self.books.values())==5:
                print("You cannot borrow more than 5 books.")
        library.borrower[self.name]=sum(self.books.values())
    def readerInfo(self,*args):
        if len(args)==0:
            print(f"{self.name}, you have {sum(self.books.values())} book(s) with you.")
            for key,value in self.books.items():
                print(f"Books on {key}:{value}")
        else:
            for x in args:
                print(f"{self.name}, you have {self.books[x]} {x} book(s) with you")
        
L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
L1.details()
print("1----------------------")
r1=Reader('Aladdin')
r1.borrow(L1,'Arts','Fiction','Fiction','Politics')
print("2----------------------")
r1.borrow(L1,'Politics','Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2=Reader('Jasmine')
r2.borrow(L1,'Politics','Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()
