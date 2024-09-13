class TaxiLagbe:
    def __init__(self,no,loca):
        self.number=no
        self.location=loca
        self.passenger={}
    def addPassenger(self,*a):
        for i in a:
            lst=i.split("_")
            if len(self.passenger)<4:
                self.passenger[lst[0]]=int(lst[1])
                print(f"Dear {lst[0]}! Welcome to TaxiLagbe.")
            else:
                print("Taxi Full! No more passengers can be added.")
    def printDetails(self):
        k=""
        to=0
        for s,m in self.passenger.items():
            k+=s+","
            to+=m
        print(f"Trip info for Taxi number: {self.number}\nThis taxi can only cover the {self.location} area. ")
        print(f"Total passengers: {len(self.passenger)}\nPassenger lists:{k}\nTotal collected fare: {to}")
taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200','Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115', 'Parker_215')
print('-------------------------------')
taxi2.printDetails()
