class MangoTree:
    def __init__(self,name):
        self.variety=name
        self.height=1.0
        self.number_of_mangoes=0
    def calc(self,year):
        a=self.height
        self.height=a+(3*year)
        if self.variety=="Amrapali":
          self.number_of_mangoes=15*self.height
        elif self.variety=="Gopalbhog":
            self.number_of_mangoes=10*self.height
        
mangoTree1= MangoTree("Gopalbhog")
# Display the details of the mango tree
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
mangoTree2= MangoTree("Amrapali")
# Display the details of the mango tree
print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")
print("Updated details after 5 years:")
print("=====================================")
mangoTree1.calc(5)
mangoTree2.calc(5)
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")