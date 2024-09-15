class NikeBangladesh:
    branchs=[]
    stocked={'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    sold=0
    def __init__(self,branch):
        self.branch=branch
        NikeBangladesh.branchs.append(self.branch)
        self.branch_product={'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    def details(self):
        print(f"Nike {self.branch} outlet:\nProducts Currently Stocked:{NikeBangladesh.stocked}\nSold: {NikeBangladesh.sold} ")
    def restockProducts(self,dic1):
        for i,j in dic1.items():
            if i in self.branch_product:
                self.branch_product[i]+=j
            if i in NikeBangladesh.stocked:
                NikeBangladesh.stocked[i]+=j
    def productSold(self,dic1):
        for i,j in dic1.items():
            if i in self.branch_product:
                self.branch_product[i]-=j
            if i in NikeBangladesh.stocked:
                NikeBangladesh.stocked[i]-=j
                NikeBangladesh.sold+=j
    @classmethod
    def status(cls):
        print(f"Nike Bangladesh Status:\nBranches Opened:{len(cls.branchs)}\nCurrently Stocked: {cls.stocked}\nSold: {cls.sold}")
print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts(
{"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts(
{"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
