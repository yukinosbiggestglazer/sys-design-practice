class Account:
	def __init__ (self, name, balance, id):
		self.name = name
		self.balance = balance
		self.id = id
		
	def withdraw(self, amt):
		if self.balance >= amt:
			self.balance -=amt
			print(self.name, amt, "succesfully withdrawn")
			return True
		else:
			print(self.name, "insufficient balance")
			return False
	
	def deposit(self, amt):
		if amt <= 0:
		    print(self.name, "invalid amount")
		    return False
		self.balance += amt
		print(self.name, "deposit successful")
		return True
		
	def show(self):
		print("Name :", self.name, "\nBalance :", self.balance, "\nID :", self.id)
		
class Bank:
	def __init__ (self):
		self.accounts = {}
	
	def open_account (self, name, balance, id):
		acc = Account(name, balance, id)
		self.accounts[id] = acc
		
	def show_all (self):
	 	for acc in self.accounts.values(): getattr(acc, "show") ()
	 	
	def transfer (self, id1, id2, balance):
		if (self.accounts[id1].withdraw(balance)):
			self.accounts[id2].deposit(balance)
			print ("succesful transfer")
		else :
			print ("insufficient balance")
		
bank = Bank()
bank.open_account("John", 150, 1)
bank.open_account("Jay", 100, 2)
bank.show_all()

bank.transfer(1, 2, 100)
bank.show_all()
bank.transfer(1, 2, 100)
