class Account():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def greet(self): # welcoming the client
        print(f"Hello {self.name}, Welcome to your bank account ! ")
    
    def deposit(self,amount): # method to add an amount of your account
        self.balance += amount
        print("Amount added successfully !")

    def withdraw(self,amount): # method to withdraw an amount of money
        self.balance -= amount
        print("Amount withdrawed successfully !") 

    @property # allows to access the method like an attribut (show and modify) 
    def get_balance(self):
        return self.balance # only use to have the balance of the bank account
    
    