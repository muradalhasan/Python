class BankAccount:
    def __init__(self,name,typ):
        self.user_name=name
        self.account_type=typ
        self.balance=1.0
    def details(self):
        print(f"New account balance of {self.user_name} is {self.balance}")
account1 = BankAccount("Bilbo", "Savings")
print("=====================================")
print(f"User Name: {account1.user_name}")
print(f"Balance: {account1.balance}")
print(f"Account Type:", account1.account_type)
print("=====================================")
account2 = BankAccount("Frodo", "Business")
print(f"User Name: {account2.user_name}")
print(f"Balance: {account2.balance}")
print(f"Account Type: {account2.account_type}")
print("=====================================")
account1.balance=15.75
account2.balance=700.5
account1.details()
account2.details()
