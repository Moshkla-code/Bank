class BankAccount:
    def __init__(self, name, balance=0):
         self.name = name 
         self.balance = balance 
    def deposit(self , amount):
         self .balance += amount
         print(f"Withdraw:{amount}, Remaining Balance:{self.balance}") 
    def withdraw(self, amount):
        if amount <= self.balance:
             self.balance -= amount
             print(f"Withdraw:{amount}, Remaining Balance:{self.balance}")
        else: print("!")  
print("--- welcome to the Bank ---") 
user__name = input("Enter your name: ")   
my_acc = BankAccount(user__name, 10000) 
print("Hello " + my_acc.name ) 
amount = float(input("How much do you want to withdraw? ")) 
my_acc.withdraw(amount)               