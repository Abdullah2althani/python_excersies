class BankAccount:
    def __init__(self, int_rate, balance): 
        self.name = name
        self.int_rate = int_rate
        self.balance = 0

	def deposit(self, amount):
		self.balance += amount
        return self
        
    def withdraw(self, amount):
        if (self.balance - amount < 0):
            print(f"Insufficient funds: Charging a {amount} fee")
		else
            self.balance -= amount
        return self
    def display_account_info(self):
		print(self.account_balance)
        return self

    def yield_interest(self):
		self.balance * self.int_rate
        return self

me = BankAccount(50, 100)
me1 = BankAccount(10, 500)

me.deposit(33).deposit(22).deposit(14).withdraw(60).yield_interest()
me2.deposit(43).deposit(62).withdraw(10).withdraw(90).withdraw(80).yield_interest()