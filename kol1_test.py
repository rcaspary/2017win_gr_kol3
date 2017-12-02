import unittest
from kol1 import *

class ClientTest(unittest.TestCase):

    #0
    def setUp(self):
        self.name = "Anna"
        self.surname = "Kowalski"
        self.balance = 400
        self.history = []
        self.exampleClient = Client(self.name, self.surname, self.balance)

    #1
    def test_init(self):
        self.assertEqual(self.exampleClient.name, self.name)
        self.assertEqual(self.exampleClient.surname, self.surname)
        self.assertEqual(self.exampleClient.balance, self.balance)
        self.assertEqual(self.exampleClient.history, self.history)

    #2
    def test_change_balance(self):
        amount = 500
        self.balance += amount
        info = "Testinfo"
        self.history.append(info)
        self.exampleClient.change_balance(amount, info)
        self.assertEqual(self.exampleClient.balance, self.balance)
        self.assertEqual(self.exampleClient.history, self.history)

    #3
    def test_get_info(self):
        info = [self.name, self.surname, self.balance, self.history]
        self.assertEqual(self.exampleClient.get_info(), info)

class BankTest(unittest.TestCase):

    def setUp(self):
        self.bank_name = "myBank"
        self.name = "Anna"
        self.surname = "Kowalski"
        self.balance = 400
        self.acc_nbr = "0001-0001"

    def setToZero(self):
        Bank.next_bank_id = 1
        self.exampleBank = Bank(self.bank_name) 
      #  self.exampleBank.bank_id = 1
      #  self.exampleBank.next_bank_id = 2
        self.dict_of_clients = {}
        self.next_client_id = 1
        self.myhistory = []

    def setTwoClients(self):
        self.setToZero()
        self.acc_nbr1 = self.exampleBank.add_client(self.name, self.surname, self.balance)
        self.acc_nbr2 = self.exampleBank.add_client(self.name, self.surname, self.balance*2)
        self.Client1 = self.exampleBank.dict_of_clients[self.acc_nbr1]
        self.Client2 = self.exampleBank.dict_of_clients[self.acc_nbr2]
        self.dict_of_clients[self.acc_nbr1] = self.Client1
        self.dict_of_clients[self.acc_nbr2] = self.Client2
    #4
    def test_init(self):
        self.setToZero()
        self.assertEqual(self.exampleBank.bank_name, self.bank_name)
        self.assertEqual(self.exampleBank.bank_id, 1)
        self.assertEqual(self.exampleBank.dict_of_clients, self.dict_of_clients)
        self.assertEqual(self.exampleBank.next_client_id, 1)
        self.assertEqual(self.exampleBank.next_bank_id, 2)

    #5
    def test_add_client(self):
        self.setToZero()
        my_acc_nbr = self.exampleBank.add_client(self.name, self.surname, self.balance)
        self.dict_of_clients[self.acc_nbr] = self.exampleBank.dict_of_clients[my_acc_nbr]
        self.assertEqual(my_acc_nbr, self.acc_nbr)
        self.assertEqual(self.exampleBank.next_client_id, self.next_client_id+1)
        self.assertEqual(self.exampleBank.dict_of_clients[self.acc_nbr].name, self.name)
        self.assertEqual(self.exampleBank.dict_of_clients[self.acc_nbr].surname, self.surname)
        self.assertEqual(self.exampleBank.dict_of_clients[self.acc_nbr].balance, self.balance)      

    #6
    def test_input_money(self):
        self.setTwoClients()
        self.exampleBank.input_money(self.acc_nbr1, self.balance)
        myinfo = {"Title": "Money imput", "Amount": self.balance}
        self.myhistory.append(myinfo)
        self.assertEqual(self.Client1.balance, self.balance*2)
        self.assertEqual(self.Client1.history, self.myhistory)

    #7
    def test_withdraw_money(self):
        self.setTwoClients()
        self.exampleBank.withdraw_money(self.acc_nbr1, 100)
        myinfo = {"Title": "Money withdraw", "Amount": 100}
        self.myhistory.append(myinfo)
        self.assertEqual(self.Client1.balance, self.balance-100)
        self.assertEqual(self.Client1.history, self.myhistory)

    #8
    def test_transfer(self):
        self.setTwoClients()
        self.assertEqual(self.Client1.balance, self.balance)
        self.assertEqual(self.Client2.balance, self.balance*2)
        self.exampleBank.transfer(self.acc_nbr2, self.acc_nbr1, self.balance)
        myinfo = {"Transfer from": self.acc_nbr2, "Amount": self.balance}
        self.myhistory.append(myinfo)
        self.assertEqual(self.Client1.balance, self.balance*2)
        self.assertEqual(self.Client2.balance, self.balance)
        self.assertEqual(self.Client1.history, self.myhistory)
        
    #9
    def test_get_transfer(self):
        self.setTwoClients()
        self.assertEqual(self.Client1.balance, self.balance)
        self.assertEqual(self.Client2.balance, self.balance*2)
        self.exampleBank.get_transfer(self.acc_nbr2, self.acc_nbr1, self.balance) 
        self.assertEqual(self.Client1.balance, self.balance*2)

    #10
    def test_info(self):
        self.setTwoClients()
        self.myhistory.append({"Title": "Money imput", "Amount": 100})
        self.myhistory.append({"Title": "Money withdraw", "Amount": 200})
        self.myhistory.append({"Transfer from": self.acc_nbr2, "Amount": 300})
        self.myhistory.append({"Transfer to": self.acc_nbr2, "Amount": 300})
        self.exampleBank.input_money(self.acc_nbr1, 100)
        self.exampleBank.withdraw_money(self.acc_nbr1, 200)
        self.exampleBank.transfer(self.acc_nbr2, self.acc_nbr1, 300)
        self.exampleBank.transfer(self.acc_nbr1, self.acc_nbr2, 300)
        self.assertEqual(self.exampleBank.dict_of_clients[self.acc_nbr1].history, self.myhistory)

class SystemTest(unittest.TestCase):

    #0
    def setUp(self):
	self.dict_of_banks = {}
	self.dict_of_banks_names = {}
	self.dict_of_all_clients = {}
        self.bank_name = "myBank"
        self.name = "Anna"
        self.surname = "Kowalski"
        self.balance = 400
    
    #11
    def test_banks_info(self):
        System.dict_of_banks = {}
        System.dict_of_banks_names = {}
        exampleBank = Bank(self.bank_name)
        bank_id = exampleBank.bank_id
        self.dict_of_banks[bank_id] = [exampleBank, self.bank_name]
        self.dict_of_banks_names[self.bank_name] = [exampleBank, bank_id]
        self.assertEqual(System.dict_of_banks, self.dict_of_banks)
        self.assertEqual(System.dict_of_banks_names, self.dict_of_banks_names)

    #12
    def test_clients_info(self):
        System.dict_of_all_clients = {}
        exampleBank = Bank(self.bank_name)
        acc_nbr1 = exampleBank.add_client(self.name, self.surname, self.balance)
        self.dict_of_all_clients[acc_nbr1] = [self.name, self.surname]
        self.assertEqual(System.dict_of_all_clients, self.dict_of_all_clients)

    #13
    def test_input_money(self):
        System.dict_of_banks = {}
        exampleBank = Bank(self.bank_name)
        acc_nbr1 = exampleBank.add_client(self.name, self.surname, self.balance)
        System.input_money(acc_nbr1, self.balance)
        self.assertEqual(exampleBank.dict_of_clients[acc_nbr1].balance, self.balance*2)

    #14
    def test_withdraw_money(self):
        System.dict_of_banks = {}
        exampleBank = Bank(self.bank_name)
        acc_nbr1 = exampleBank.add_client(self.name, self.surname, self.balance)
        System.withdraw_money(acc_nbr1, self.balance)
        self.assertEqual(exampleBank.dict_of_clients[acc_nbr1].balance, 0)        

    #15
    def test_get_bank_ref(self):
        System.dict_of_banks = {}
        exampleBank = Bank(self.bank_name)
        self.assertEqual(System.dict_of_banks[exampleBank.bank_id][0], exampleBank)
