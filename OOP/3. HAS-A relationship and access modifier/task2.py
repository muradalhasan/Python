class Spaceship:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
        self.metals=[]
    def load_cargo(self,a):
        if a.getWeight()<=self.weight:
            self.metals.append(a.getName())
            print(f"Spaceship Name:{a.getWeight()}\nCapacity:{self.weight}")
            self.weight-=a.getWeight()
        else:
            print("Warning: Unable to load Neutronium inside Falcon. Exceeds capacity by 75000.")
    def  display_details(self):
        print(self.metals)
class Cargo:
    def __init__(self,name,weight):
        self.__name=name
        self.__weight=weight
    def getName(self):
        return self.__name
    def getWeight(self):
        return self.__weight
    
falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold)  # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium)  # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium)  # This should not exceed Enterprise's capacity
enterprise.display_details()
