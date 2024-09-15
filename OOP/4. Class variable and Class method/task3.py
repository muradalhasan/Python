class Foodiz:
    number_of_branch=0
    revenue=0
    branches={}
    def __init__(self,name):
        self.branch_name=name
        self.branch_sell=0
        Foodiz.number_of_branch+=1
    def sellQuantity(self,quan):
        self.branch_sell+=300*quan
        Foodiz.revenue+=self.branch_sell
        if self.branch_name not in Foodiz.branches:
            Foodiz.branches[self.branch_name]=self.branch_sell
        else:
            Foodiz.branches[self.branch_name]+=self.branch_sell
    def branchInformation(self):
        print(f"Branch Name: {self.branch_name}\nBranch Sell: {self.branch_sell}")
    @classmethod
    def details(cls):
        print(f"Total Number of branch(s):{cls.number_of_branch}\nTotal Sell:{cls.revenue}")
        if len(cls.branches)!=0:
            for i,j in cls.branches.items():
                print(f"Branch Name: {i}\nBranch Sell: {j}")
                cont=(j/cls.revenue)*100
                print(f"Branch consists of total sell's: {cont}")
Foodiz.details()
print('1----------------------------------')
mohakhali = Foodiz('Mohakhali')
mohakhali.sellQuantity(25)
mohakhali.branchInformation()
print('2----------------------------------')
Foodiz.details()
print('3========================')
banani = Foodiz('Banani')
banani.sellQuantity(15)
banani.branchInformation()
print('4----------------------------------')
Foodiz.details()
print('5========================')
gulshan = Foodiz('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('6----------------------------------')
Foodiz.details()



