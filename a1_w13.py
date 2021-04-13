'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210413]                                   ##
#*******************************************************************************************#
#############################################################################################
'''

# Class4-DatabaseModule-Week13
# Add and implement a MongoDB connection to either your Youtube Video Downloader App (assignment of 4th week) or 
# your Python Module Project App. Use MongoDB Atlas as your cloud database and with the help of PyMongo, 
# connect to the database and perform at least two of the CRUD operations. 
# You can ignore the authentication, security etc. for now. Just perform two different types of simple CRUD operations.

#  >>-------------->  I ADDED dbWrite() AND dbDelete() methods. <--------------<<

import datetime
import fileinput
import os
import re
import sys

from pymongo import MongoClient
from bson.json_util import dumps

x = datetime.datetime.now()
t = x.strftime("%c")

if os.path.isfile('bankdata.txt'):
    pass
else:
    with open("bankdata.txt", "w+"):        
        print('Necessary txt file created')

class User:
    '''
    -I ADDED dbWrite() AND dbDelete() methods. (date of add: 13/04/2021)
    '''
    current_user_info = []

    def __init__(self, name="", surname="", ID=""):
        self.name = name
        self.surname = surname
        self.ID = ID
        self.email = self.name + "." + self.surname + "@csbank.com"
        self.data_list = self.read_txt('bankdata.txt')

    def login(self, dataList):
        while True:  # 2 bilginin dogru girilmesiye birlikte User sinifi menusu calisir.
            print('\t'.expandtabs(12), 33 * '=' + " WELCOME, Please LOGIN first " + 33 * '=')
            print()
            self.name = input("\t\t\t Enter a current customer NAME: ")
            if self.name.isalpha() and len(self.name) > 2:
                self.ID = input("\t\t\t Enter a current customer ID: ")
                if self.ID.isdigit() and int(self.ID) > 0 and len(self.ID) > 2:
                    for current_user in dataList:
                        if current_user[0] == self.ID and current_user[1] == self.name:
                            print("\nWelcome {}, \nLogin is successful!".format(self.name).upper())
                            User.current_user_info = current_user
                            print(User.current_user_info)
                            self.main_menu(current_user)
                    else:
                        print("---> Invalid user NAME or ID! Try again <---")
                else:
                    print("You have to enter least 3 DIGIT!")
            else:
                print("You have to enter least 3 LETTER!")

    def create_user(self):
        while True:
            try:
                print("You have to enter least 3 digit!")
                self.name = input("Enter a NAME: ")
                self.surname = input("Enter a SURNAME: ")
                self.ID = input("Enter a ID No: ")
                money = input("The amount of MONEY deposited:")
                self.email = self.name + "." + self.surname + "@csbank.com"
                if len(self.ID) > 2 and len(self.name) > 2:
                    break
            except:
                print("You have to enter least 3 digit!")

        with open("bankdata.txt", "r+") as f:
            for line in f:
                line = line.rstrip()
                nesne1 = re.search(self.ID, line)
                nesne2 = re.search(self.name, line)
                if nesne1 and nesne2:
                    print("Sorry! This NAME and ID are in use.")
                    break
            else:
                f.write(self.ID + "\t\t")
                f.write(self.name + "\t\t")
                f.write(self.surname + "\t\t")
                f.write(self.email + "\t\t")
                f.write(money + "\t\t")  # mevcut balans i txt ye yazdim.
                f.write(t + " \n")  # islem tarihini txt ye yazdim.
                f.seek(0)
                print("Registration is done!")                
                   
    def dbWrite(self):
        '''
        -cagrildiginda; bankdata.txt dosyasinda kayitli tum musteri bilgilerinin son halini mongodb database e insert eder.
        -logout() metodu cagrildiginda cikis yapmilmadan hemen oncesinde database e son guncel bilgiler dbWrite() ile kaydolur. 
        '''
        uri = "mongodb://semih:fsm1453.@pycoderscluster-shard-00-00.gqmuc.mongodb.net:27017,pycoderscluster-shard-00-01.gqmuc.mongodb.net:27017,pycoderscluster-shard-00-02.gqmuc.mongodb.net:27017/AtmProject?ssl=true&replicaSet=atlas-u055i5-shard-0&authSource=admin&retryWrites=true&w=majority"
        # a MongoClient object
        client = MongoClient(uri)
        db= client.AtmProject        
        us = db.users
        
        mykeys = ['customer_id','name','surname','email','balance','TransactionDate']
        d = self.read_txt('bankdata.txt')
        di = dict()
        
        for i in d:
            n = 0
            for j in i:
                di[mykeys[n]] = j 
                n += 1
                   
            insert_result = us.insert_one(di)
            di.clear()
        print("Successful! All data updated.")
        
    def dbDelete(self):
        uri = "mongodb://semih:fsm1453.@pycoderscluster-shard-00-00.gqmuc.mongodb.net:27017,pycoderscluster-shard-00-01.gqmuc.mongodb.net:27017,pycoderscluster-shard-00-02.gqmuc.mongodb.net:27017/AtmProject?ssl=true&replicaSet=atlas-u055i5-shard-0&authSource=admin&retryWrites=true&w=majority"
        
        client = MongoClient(uri)
        db= client.AtmProject        
        us = db.users
        name = input("Enter a NAME (for delete in db): ")
        # dr = us.delete_one({'name': name})
        dr = us.delete_many({'name': name})
        print('Deleted count: ',dr.deleted_count)        
        
    def read_txt(self, file_txt):
        f = open(file_txt, 'r')
        lines_list = []
        for line in f:
            line = line.rstrip().split("\t\t")
            lines_list.append(line)
        f.close()        
        return lines_list  # lines_list = TUM musteri bilgileri listelerinin listesi

    def fileInput(self, searchExp, replaceExp):
        for line in fileinput.input('bankdata.txt', inplace=1):
            if searchExp in line:
                line = line.replace(searchExp, replaceExp)
            sys.stdout.write(line)

    def find_user(self, id):
        for i in self.data_list:
            if i[0] == id:
                return i

    def edit_user(self):  # liste = [id,name,surname,email,balance,date] currrent customer info.
        f = self.find_user(User.current_user_info[0])
        q = input("Which information will be updated? \nNAME    --> 1, \nSURNAME --> 2 \ne-mail  --> 3 \nChoice:..")
        if q == '1':
            new_name = input("Enter a NEW name:")
            self.fileInput(f[1], new_name)
            self.fileInput(f[5], t)
            print("The name has been changed \nYou must have again login..")
        if q == '2':
            new_surname = input("Enter a NEW surname:")
            self.fileInput(f[2], new_surname)
            self.fileInput(f[5], t)
            print("The surname has been changed \nYou must have again login..")
        if q == '3':
            new_email = input("Enter a NEW email:")
            self.fileInput(f[3], new_email)
            self.fileInput(f[5], t)
            print("The mail has been changed \nYou must have again login..")
        self.logout()

    def start(self):
        if len(self.data_list) == 0:
            self.data_list.append(['111', 'semih', 'can', 'semih.can@csbank.com', '100', t])
            u.login(self.data_list)
        else:
            u.login(self.data_list)

    def logout(self):
        print("{} quit the application..".format(self.name).upper())
        
        # u.dbWrite()                 # database i gunceller ve ardindan cikis yapar.
        
        exit()
        
    def delete_user2(self,name):
        pass

    def delete_user(self):
        f = open("bankdata.txt", "r+")
        copy = open("bankdata2.txt", "w+")
        self.name = input("Enter customer NAME to be deleted: ")
        self.surname = input("Enter customer SURNAME to be deleted: ")
        self.ID = input("Enter customer ID to be deleted: ")
        for line in f:
            nesne1 = re.search(self.name, line)
            nesne2 = re.search(self.ID, line)
            if nesne1 and nesne2:
                print("Your account is DELETED! ")
                continue
            else:
                copy.write(line)
        f = open("bankdata.txt", "w")  # ilk dosyanin icini sildim.
        with open("bankdata2.txt", "r+") as copy:
            with open("bankdata.txt", "w+") as f:
                for line in copy:
                    f.write(line)
        self.logout()

    def main_menu(self, i): # i = current_user list.
        while True:
            menu = ["+------ Welcome to C&S Bank ------+",
                    "|  1. NEW Customer                |",
                    "|  2. Edit Customer Information   |",
                    "|  3. Delete Customer Account     |",
                    "|  4. Transaction_menu...         |",
                    "|  5. L o g o u t                 |",
                    "|  6. NEW!--> Db delete a customer|",
                    "|  7. NEW!--> Db update           |"]
            for j in menu:
                print('\t'.expandtabs(44), j)
            print("ID: {}\nName: {}\nSurname: {}\nMail: {}\n".format(i[0], i[1], i[2], i[3]))
            choice = input("Enter your choice:...")
            if choice == "1":
                u.create_user()  # User class in create_user() methodu calisir.
            elif choice == "2":
                u.edit_user()  # User class in edit_user() methodu calisir.
            elif choice == "3":
                u.delete_user()  # User class in delete_user() methodu calisir.
            elif choice == "4":
                Bank.transaction_menu(self)  # Bank class in transaction_menu() methodu calisir.
            elif choice == "5":                
                u.logout()  # User class in logout() methodu calisir.
            elif choice == "6":                
                u.dbDelete()  
            elif choice == "7":                
                u.dbWrite()  
            else:
                print("Something went wrong. Try again later..")


class Bank(User):

    def __init__(self, balance=''):
        super().__init__()
        self.balance = balance

    def getBalance(self, currentUserInfo):
        b = User.find_user(self, currentUserInfo[0])
        print("your balance: {}$ \nLast transaction date: {}".format(b[4], b[5]))
        return b[4]

    def deposit(self, currentUserInfo):
        amount = int(input("Enter the amount to DEPOSIT: "))
        a = int(currentUserInfo[4])
        a += amount
        print("\nYour current BALANCE is:", a, '$')
        b = User.find_user(self, currentUserInfo[0])
        self.fileInput(b[4], str(a))
        self.fileInput(b[5], t)
        u.logout()

    def withdraw(self, currentUserInfo):
        amount = int(input("Enter the amount to WITHDRAW: "))
        a = int(currentUserInfo[4])
        if a >= amount:
            a -= amount
            print("\nYour current BALANCE is:", a, '$')
            b = User.find_user(self, currentUserInfo[0])
            self.fileInput(b[4], str(a))
            self.fileInput(b[5], t)
            u.logout()
        else:
            print("\nBalance is insufficient  ")
            print("\nYour current BALANCE is:", a, '$')

    def transfer(self, currentUserInfo):
        self.getBalance(currentUserInfo)
        id_number = input("Enter the ID of Customer to be transferred: ")
        if id_number != currentUserInfo[0]:
            for j in self.data_list:
                if j[0] == id_number:
                    print("Client has been found")
                    break

            amount = int(input("Enter the AMOUNT to transfer: "))
            a = int(currentUserInfo[4])
            if a >= amount:
                a -= amount
                b = User.find_user(self, currentUserInfo[0])
                self.fileInput(b[4], str(a))
                self.fileInput(b[5], t)

                f = User.find_user(self, id_number)
                result = int(f[4])
                result += amount
                self.fileInput(f[4], str(result))
                self.fileInput(f[5], t)

                print("Transfer done! \nYou must have again login..")
                self.transaction_menu()
            else:
                print("\nBalance is insufficient  ")
                print("\nYour current balance is:", self.getBalance(currentUserInfo) + '$')
                self.transaction_menu()
        else:
            print("Error! Both the same account number..\nExits the application.")
            exit()

    def transaction_menu(self):
        while True:
            menu = ["+------ Transaction Menu ------+",
                    "|   1. Get Balance             |",
                    "|   2. Deposit Money           |",
                    "|   3. Withdraw                |",
                    "|   4. Transfer Money          |",
                    "|   5. Back to Main Menu...    |",
                    "|   6. Logout                  |"]
            for i in menu:
                print('\t'.expandtabs(55), i)
            choice = input("Enter your choice:...")
            if choice == "1":
                c.getBalance(User.current_user_info)
            elif choice == "2":
                c.deposit(User.current_user_info)
            elif choice == "3":
                c.withdraw(User.current_user_info)
            elif choice == "4":
                c.transfer(User.current_user_info)
            elif choice == "5":
                c.main_menu(User.current_user_info)
            elif choice == "6":
                c.logout()
            else:
                print("Something went wrong. Try again Please...")


u = User()
c = Bank()
u.start()

