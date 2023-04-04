class SultansDine:
    total_sell=0
    total_branch=0
    branch_list=[]
    def __init__(self,branch):
        SultansDine.total_branch+=1
        SultansDine.branch_list.append(self)
        self.branch=branch
        self.sell=0
        self.percentage_of_total_sell=0
    def sellQuantity(self,quantity):
        if quantity < 20:
            if quantity < 10:
                self.sell+=quantity*300
            else:
                self.sell+=quantity*350
        else:
            self.sell+=quantity*400
        SultansDine.total_sell+=self.sell
        for x in SultansDine.branch_list:
            x.percentage_of_total_sell=round(((x.sell/SultansDine.total_sell)*100),2)
    def branchInformation(self):
        print(f"Branch Name: {self.branch}\nBranch Sell: {self.sell}")
    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {cls.total_branch}\nTotal Sell: {cls.total_sell} Taka")
        if SultansDine.total_branch!=0:
            for x in SultansDine.branch_list:
                print(f"Branch Name: {x.branch}, Branch Sell: {x.sell} Taka\nBranch consists of total sell's: {x.percentage_of_total_sell}%")

SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()
