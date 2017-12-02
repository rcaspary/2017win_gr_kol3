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

    #4
    def test_init(self):
        bank_id = 2
        next_bank_id = bank_id +1
        dict_of_clients = {}
        next_client_id = 1
        exampleBank = Bank(self.bank_name)
        self.assertEqual(exampleBank.bank_name, self.bank_name)
        self.assertEqual(exampleBank.bank_id, exampleBank.next_bank_id-1)     #fail
        self.assertEqual(exampleBank.dict_of_clients, dict_of_clients)
        self.assertEqual(exampleBank.next_client_id, next_client_id)
        self.assertEqual(exampleBank.next_bank_id, exampleBank.bank_id+1)

    #5
    def test_add_client(self):
        dict_of_clients = {}
        next_client_id = 2
        exampleBank = Bank(self.bank_name)
        my_acc_nbr = exampleBank.add_client(self.name, self.surname, self.balance)
        dict_of_clients[self.acc_nbr] = exampleBank.dict_of_clients[my_acc_nbr]
        self.assertEqual(my_acc_nbr, self.acc_nbr)
        self.assertEqual(exampleBank.next_client_id, next_client_id)
        self.assertEqual(exampleBank.dict_of_clients[self.acc_nbr].name, self.name)
        self.assertEqual(exampleBank.dict_of_clients[self.acc_nbr].surname, self.surname)
        self.assertEqual(exampleBank.dict_of_clients[self.acc_nbr].balance, self.balance)      

    #6
    def test_input_money(self):
        dict_of_clients = {}
        exampleBank = Bank(self.bank_name)
        my_acc_nbr = exampleBank.add_client(self.name, self.surname, self.balance)        
        dict_of_clients[my_acc_nbr] = exampleBank.dict_of_clients[my_acc_nbr]
        exampleBank.input_money(my_acc_nbr, self.balance)
        myClient = exampleBank.dict_of_clients[my_acc_nbr]
        myinfo = {"Title": "Money imput", "Amount": self.balance}
        myhistory = []
        myhistory.append(myinfo)
        self.assertEqual(myClient.balance, self.balance*2)
        self.assertEqual(myClient.history, myhistory)

    #7
    def test_withdraw_money(self):
        dict_of_clients = {}
        exampleBank = Bank(self.bank_name)
        my_acc_nbr = exampleBank.add_client(self.name, self.surname, self.balance)        
        dict_of_clients[my_acc_nbr] = exampleBank.dict_of_clients[my_acc_nbr]
        exampleBank.withdraw_money(my_acc_nbr, self.balance)
        myClient = exampleBank.dict_of_clients[my_acc_nbr]
        myinfo = {"Title": "Money withdraw", "Amount": self.balance}
        myhistory = []
        myhistory.append(myinfo)
        self.assertEqual(myClient.balance, 0)
        self.assertEqual(myClient.history, myhistory)

    #8
    def test_transfer(self):
        dict_of_clients = {}
        exampleBank = Bank(self.bank_name)
        acc_nbr1 = exampleBank.add_client(self.name, self.surname, self.balance)
        acc_nbr2 = exampleBank.add_client(self.name, self.surname, self.balance*2)
        Client1 = exampleBank.dict_of_clients[acc_nbr1]
        Client2 = exampleBank.dict_of_clients[acc_nbr2]
        dict_of_clients[acc_nbr1] = Client1
        dict_of_clients[acc_nbr2] = Client2
        self.assertEqual(Client1.balance, self.balance)
        self.assertEqual(Client2.balance, self.balance*2)
        exampleBank.transfer(acc_nbr2, acc_nbr1, self.balance)
        self.assertEqual(Client1.balance, self.balance*2)
        self.assertEqual(Client2.balance, self.balance)
        
    #9
    def test_get_transfer(self):
        dict_of_clients = {}
        exampleBank = Bank(self.bank_name)
        acc_nbr1 = exampleBank.add_client(self.name, self.surname, self.balance)
        acc_nbr2 = exampleBank.add_client(self.name, self.surname, self.balance*2)
        Client1 = exampleBank.dict_of_clients[acc_nbr1]
        Client2 = exampleBank.dict_of_clients[acc_nbr2]
        dict_of_clients[acc_nbr1] = Client1
        dict_of_clients[acc_nbr2] = Client2
        self.assertEqual(Client1.balance, self.balance)
        self.assertEqual(Client2.balance, self.balance*2)
        exampleBank.get_transfer(acc_nbr2, acc_nbr1, self.balance)
        self.assertEqual(Client1.balance, self.balance*2)

    #10
    def test_info(self):
        dict_of_clients = {}
        exampleBank = Bank(self.bank_name)
        acc_nbr1 = exampleBank.add_client(self.name, self.surname, self.balance)
        acc_nbr2 = exampleBank.add_client(self.name, self.surname, self.balance*2)
        Client1 = exampleBank.dict_of_clients[acc_nbr1]
        Client2 = exampleBank.dict_of_clients[acc_nbr2]
        dict_of_clients[acc_nbr1] = Client1
        dict_of_clients[acc_nbr2] = Client2
        myhistory = []
        myhistory.append({"Title": "Money imput", "Amount": 100})
        myhistory.append({"Title": "Money withdraw", "Amount": 200})
        myhistory.append({"Transfer from": acc_nbr2, "Amount": 300})
        myhistory.append({"Transfer to": acc_nbr2, "Amount": 300})
        exampleBank.input_money(acc_nbr1, 100)
        exampleBank.withdraw_money(acc_nbr1, 200)
        exampleBank.transfer(acc_nbr2, acc_nbr1, 300)
        exampleBank.transfer(acc_nbr1, acc_nbr2, 300)
        self.assertEqual(exampleBank.dict_of_clients[acc_nbr1].history, myhistory)


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
        self.acc_nbr = "0001-0001"
    
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





        
      
        
