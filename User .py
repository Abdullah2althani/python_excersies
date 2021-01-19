class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

me = User("Michael", "michael@codingdojo.com")
me1 = User("Ali", "Ali@codingdojo.com")
me2 = User("Ahmed", "Ahmed@codingdojo.com")

me.make_deposit(50).make_deposit(50).make_deposit(50).make_withdrawal(20).display_user_balance()
me1.make_deposit(50).make_deposit(50).make_withdrawal(20).make_withdrawal(20).display_user_balance()
me2.make_deposit(150).make_withdrawal(10).make_withdrawal(50).make_withdrawal(20).display_user_balance()

