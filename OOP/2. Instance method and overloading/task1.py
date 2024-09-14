class Customer:
    def __init__(self):
        self.ticket={}
        print("Welcome to ABC Memorial Park ")
    def buyTicket(self,name,age):
        if len(self.ticket)<3:
            self.ticket[name]=age
            print(f"Successfully purchased a ticket for {name}! ")
        else:
            print("You can't buy more than 3 tickets ")
    def showDetails(self):
        total=0
        for i,j in self.ticket.items():
            if j>10:
                total+=100
            else:
                total+=50
        print(f"Amount of tickets: {len(self.ticket)}\nTotal price: {total} Taka ")
print('1-------------------------') 
customer1 = Customer() 
print('2-------------------------') 
customer1.buyTicket('Bob', 23) 
customer1.buyTicket('Henry', 7) 
customer1.buyTicket('Alexa', 30) 
customer1.buyTicket('Jonas', 43) 
print('3-------------------------') 
customer1.showDetails() 
print('4-------------------------') 
customer2 = Customer() 
print('5-------------------------') 
customer2.buyTicket('Harry', 60) 
customer2.buyTicket('Tomas', 28) 
print('6-------------------------') 
customer2.showDetails()

