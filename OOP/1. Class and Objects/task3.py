class Contacts:
    def __init__(self,name,numbers):
        self.name=name
        self.numbers=numbers
        self.contactDict={}
        if len(name)!=len(numbers):
            print("Contacts cannot be saved. Length Mismatch!")
        else:
            print("Contacts saved successfully.")
            for i in range(len(name)):
                self.contactDict[name[i]]=numbers[i]
            
names = ["Emergency", "Father", "Bestie"]
numbers = ["999", "01xx23", "01xx87", "01xx65", "01xx43"]

m1 = Contacts(names, numbers)
print("Saved Contacts:", m1.contactDict)
print("---------------------------------------------")

names.append("Mother")
numbers.pop()

m2 = Contacts(names, numbers)
print("Saved Contacts:", m2.contactDict)
