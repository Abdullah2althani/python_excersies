class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = BankAccount(int_rate=0.01,balance=0)
    
    def make_deposit(self, amount):	
        self.account_balance.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.account_balance.balance)

class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = 0.01
        self.balance = 0

    def deposit(self, amount):
        self.balance+= amount
        return self
	
    def withdraw(self, amount):
        if (self.balance-amount<0):
            print(f"Insufficient funds: Charging a {amount} fee")
            return self
        else:
            self.balance-=amount
            return self
	
    def yield_interest(self):
        if self.balance>0:
            self.balance * self.int_rate
            return self
        else:
            return self

me = User("Michael", "michael@codingdojo.com")
me1 = User("Ali", "Ali@codingdojo.com")
me2 = User("Ahmed", "Ahmed@codingdojo.com")

me.make_deposit(50).make_deposit(50).make_deposit(50).make_withdrawal(20).display_user_balance()
me1.make_deposit(10).make_deposit(40).make_deposit(90).make_withdrawal(20).display_user_balance()


