#author: SinusAlfa

class Client:
	def __init__(self, name, surname, balance):
		self.name = name
		self.surname = surname
		self.balance = balance
		self.history = []

	def change_balance(self, amount, info):
		self.balance += amount
		self.history.append(info)

	def get_info(self):
		return [self.name, self.surname, self.balance, self.history]

class Bank:
	next_bank_id = 1

	def __init__(self, bank_name):
		self.bank_name = bank_name
		self.bank_id = Bank.next_bank_id
		self.dict_of_clients = {}
		self.next_client_id = 1
		Bank.next_bank_id += 1
		System.banks_info(self, self.bank_name, self.bank_id)

	def add_client(self, name, surname, balance):
		acc_nbr = str("%04d" % self.bank_id) + "-" + str("%04d" % self.next_client_id)
		self.dict_of_clients[acc_nbr] = Client(name, surname, balance)
		self.next_client_id += 1
		System.clients_info(name, surname, acc_nbr)
		return acc_nbr

	def input_money(self, acc_nbr, amount):
		info = {"Title": "Money imput", "Amount": amount}
		self.dict_of_clients[acc_nbr].change_balance(amount, info)

	def withdraw_money(self, acc_nbr, amount):
		info = {"Title": "Money withdraw", "Amount": amount}
		self.dict_of_clients[acc_nbr].change_balance(-amount, info)

	def transfer(self, sender_acc_nbr, acceptor_acc_nbr, amount):
		info = {"Transfer to": acceptor_acc_nbr, "Amount": amount}
		self.dict_of_clients[sender_acc_nbr].change_balance(-amount, info)
		System.transfer(sender_acc_nbr, acceptor_acc_nbr, amount)

	def get_transfer(self, sender_acc_nbr, acceptor_acc_nbr, amount):
		info = {"Transfer from": sender_acc_nbr, "Amount": amount}
		self.dict_of_clients[acceptor_acc_nbr].change_balance(amount, info)

	def info(self, acc_nbr):
		return self.dict_of_clients[acc_nbr].get_info()

class System:
	dict_of_banks = {}
	dict_of_banks_names = {}
	dict_of_all_clients = {}

	@staticmethod
	def banks_info(bank, bank_name, bank_id):
		System.dict_of_banks[bank_id] = [bank, bank_name]
		System.dict_of_banks_names[bank_name] = [bank, bank_id]

	@staticmethod
	def clients_info(name, surname, acc_nbr):
		System.dict_of_all_clients[acc_nbr] = [name, surname]

	@staticmethod
	def transfer(sender_acc_nbr, acceptor_acc_nbr, amount):
		bank_id = int(acceptor_acc_nbr.split("-")[0])
		System.dict_of_banks[bank_id][0].get_transfer(sender_acc_nbr, acceptor_acc_nbr, amount)

	@staticmethod
	def input_money(acc_nbr, amount):
		bank_id = int(acc_nbr.split("-")[0])
		System.dict_of_banks[bank_id][0].input_money(acc_nbr, amount)

	@staticmethod
	def withdraw_money(acc_nbr, amount):
		bank_id = int(acc_nbr.split("-")[0])
		System.dict_of_banks[bank_id][0].withdraw_money(acc_nbr, amount)

	@staticmethod
	def get_bank_ref(acc_nbr):
		bank_id = int(acc_nbr.split("-")[0])
		return System.dict_of_banks[bank_id][0]


#methods
def create_bank(name):
	if name not in System.dict_of_banks_names:
		Bank(name)
		return "Bank " + name + " has been created." 
	else:
		return name + " already in use."
	
def add_client(bank, name, surname, balance):
	balance = float(balance)
	nbr = System.dict_of_banks_names[bank][0].add_client(name, surname, balance)
	return name + " " + surname + " number is: " + nbr

def input_money(acc_nbr, amount):
	amount = float(amount)
	System.input_money(acc_nbr, amount)
	return "done"

def withdraw_money(acc_nbr, amount):
	amount = float(amount)
	System.withdraw_money(acc_nbr, amount)
	return "done"

def transfer(sender_acc_nbr, acceptor_acc_nbr, amount):
	amount = float(amount)
	System.transfer(sender_acc_nbr, acceptor_acc_nbr, amount)
	return "done"

def client(acc_nbr):
	return System.get_bank_ref(acc_nbr).info(acc_nbr)

def info():
	return System.dict_of_all_clients

def help():
	return '''
Welcome to Banking Simulator
List of all available commands:\n
\tinfo - Show info about all clients
\tclient <account number> - Show client info
\tcreate_bank <name> - Create new bank
\tadd_client <bank> <name> <surname> <balance> - Add new client to bank
\tinput_money <account number> <amount> - Input money to account number
\twithdraw_money <account number> <amount> - Withdraw money from account number
\ttransfer <from number> <to number> <amount>- Transfer amout of money
\thelp - Show list of commands
\texit - Exit
'''

if __name__ == "__main__":

	#sample clients data
	bank1 = Bank("BaBaBank")
	client1 = bank1.add_client("Ala", "Makota", 1000.20)
	#print "Ala Makota account number: " + str(client1)
	client2 = bank1.add_client("Jas", "Imalgosia", 9990.60)
	#print "Jas Imalgosia account number: " + str(client2)
	bank2 = Bank("BankAnkAnk")
	client3 = bank2.add_client("Ala", "Makota", 3000.20)
	#print "Ala Makota 2nd account number: " + str(client3)
	client4 = bank2.add_client("Janusz", "Typowy", 1410.60)
	#print "Janusz Typowy account number: " + str(client4)
	bank1.input_money(client1, 200.28)
	bank2.withdraw_money(client4, 100.39)
	bank1.transfer(client2, client4, 400)
	#print str(bank1.dict_of_clients[client1].history) + " Final balance: " + str(bank1.dict_of_clients[client1].balance)
	#print str(bank1.dict_of_clients[client2].history) + " Final balance: " + str(bank1.dict_of_clients[client2].balance)
	#print str(bank2.dict_of_clients[client3].history) + " Final balance: " + str(bank2.dict_of_clients[client3].balance)
	#print str(bank2.dict_of_clients[client4].history) + " Final balance: " + str(bank2.dict_of_clients[client4].balance)

	#read data from file
	try:
		logfile = open('data.log', 'r')
		cmd = logfile.readline().split(" ")
		#print cmd
		for i in cmd:
			if i != '':
				eval(i)
	except IOError:
		print "no data"

	#main loop
	print help()
	while True:
		#commands interpreter
		cmd = raw_input(">>: ")
		cmd_list = cmd.split(" ")
		if len(cmd_list) > 1:
			cmd = cmd_list[0] + '("'
			while "" in cmd_list:
				cmd_list.remove("")
			for i in cmd_list[1:]:
				if cmd_list.index(i) != 1:
					cmd += '"' + ',' + '"'
				cmd += i

			cmd += '")'
		elif cmd_list[0] != '':
			cmd += "()"

		try:
			if cmd != '':
				print "\t" + str(eval(cmd))

		except StandardError:
			print "\tCommand not found."

		else:
			#log commands to file
			logfile = open('data.log', 'a')
			if cmd != "exit()":
				logfile.write(cmd + " ")
logfile.close()
