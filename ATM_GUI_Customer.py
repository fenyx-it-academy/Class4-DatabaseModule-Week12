from pymongo import MongoClient

from datetime import datetime
import re
import tkinter

class Customer():
    date = datetime.now()
    trs_date = f"{date.day}\{date.month}\{date.year}"

    def __init__(self):

        self.name = None
        self.surname = None
        self.id_number = None
        self.account_number = None
        self.insert_money = None
        self.withdraw = None
        self.email = None
        self.telephone = None
        self.password = None
        self.new_email = None
        self.new_telephone = None

    def get_customer_from_txt(self, id_number):
        print(id_number)
        if str(id_number)!=".!labelframe2.!entry":
            with  open('users.txt', 'r', encoding='utf8') as file_name:
                koor = re.search(id_number, file_name.read())
                if koor != None:
                    if type(koor.span()) is tuple:
                        file_name.seek(koor.span()[0] + 1)
                        return file_name.readline()
                    else:
                        return None

    def set_customer_information(self, id_number):
        customer_text = self.get_customer_from_txt(id_number)
        if customer_text != None:
            customer_text = customer_text.split()
            self.name = customer_text[2]
            self.surname = customer_text[3]
            self.id_number = customer_text[0]
            self.telephone = customer_text[4]
            self.email = customer_text[5]
            self.password = customer_text[1]

            return True
        return False


    def change_email(self):
            with open('users.txt', 'r+', encoding='utf8') as file_name:
                file_name.seek(re.search(self.email, file_name.read()).start())
                patern = r'\w*[@]\w+[.]\D{3}'
                if type(re.search(patern, self.new_email).span()) is tuple:
                    file_name.write(f'\t{self.new_email}{" " * 5}')
                else:
                    print("Please enter valid e-mail address")
            return f'Your info updated'

    def change_telephone(self):
            with open('users.txt', 'r+', encoding='utf-8') as file_name:
                koor = re.search(self.telephone, file_name.read())
                file_name.seek(koor.start())
                if len(self.telephone) == 9:
                    file_name.write(f'\t{self.new_telephone}\t')
                else:
                    print("Please enter 9 digit telephone number")
            return f'Your info updated'

    @property
    def check_balance(self):  # amount of money(finaly)
        with  open('banktransaction.txt', 'r', encoding='utf-8') as transactions:
            koor = re.search(f'{self.id_number}', transactions.read())
            transactions.seek(koor.end())
            a = transactions.readline().split()
            return (a[-1])

    def add_money(self):
        self.new_balance(int(self.check_balance) + int(self.insert_money))
        return

    def withdraw_money(self):
        self.new_balance(int(self.check_balance) - int(self.withdraw))
        return

    def new_balance(self,amount):
        # dosya ya degisen hesap bakiyesini eklemek icin kullanilir
        # with open('banktransaction.txt', 'r+') as transactions:
        #     customer_transaction_lines_list = transactions.readlines()
        #     for customer_transaction_line in customer_transaction_lines_list:
        #         if self.id_number in customer_transaction_line:
        #             index = customer_transaction_lines_list.index(customer_transaction_line)
        #             customer_transaction_lines_list[index] = str(customer_transaction_line).strip('\n') + " Balance " + str(amount) + '\n'
        #     print(customer_transaction_lines_list[0])
        #     print(customer_transaction_lines_list[1])
        #     transactions.seek(0)
        #     transactions.writelines(customer_transaction_lines_list)

        client = MongoClient("mongodb+srv://test:12345@cluster0.qp06g.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

        bank = client.bank
        bank_customers = bank.bank_customers
        customers = ["12345678910", "12345699999","9876543210"]
        balances = [75000, 175000, 25000]

        for i in range(len(customers)):
            doc = {
                "customer": customers[i],
                "balance": balances[i],
            }

            bank_customers.insert_one(doc) # insert_one ile ekleme

        # delete_one ile silme
        deleted= bank_customers.delete_one({'balance': 25000})

        print(deleted)
        results = bank_customers.find({"balance":25000})

        for result in results:
            print(result)


class Bank:
    file_name = 0
    def __init__(self):
        pass

    def money_transfer(self, sender_id, receiver_id, amount):
        if self.is_avaliable(sender_id, amount) and self.is_user(receiver_id):
            sender_customer_1 = Customer()
            sender_customer_1.set_customer_information(sender_id)
            receiver_customer_2 = Customer()
            if receiver_customer_2.set_customer_information(receiver_id) and self.is_avaliable(sender_id, amount):
                sender_customer_1.withdraw = amount
                sender_customer_1.withdraw_money()
                receiver_customer_2.insert_money = amount
                receiver_customer_2.add_money()


    def login_id_password_check(self, id, password):
        print("kullanıcı adı veya parola hatalı")
        customer_1 = Customer()
        if customer_1.set_customer_information(id) == True:
            if customer_1.password == password:
                return True
            else:
                return False


    def is_user(self, id):
        print("alıcı customer bulunamadı")
        customer_1 = Customer()
        if customer_1.set_customer_information(id) == True:
            return True
        else:
            return False


    def is_avaliable(self,id, amount):
        print("gönderici bakiyesi yeterli değil")
        customer_1 = Customer()
        if customer_1.set_customer_information(id) == True:
            if int(customer_1.check_balance) >= int(amount):
                return True
            else:
                return False
        else:
            return False

# obje = Customer()
# obje.set_customer_information('12345699999')
#
# obje_1 = Customer()
# obje_1.set_customer_information('12345678910')
#
# print(obje.name)
# print(obje.surname)
# print(obje.password)
# print(obje.id_number)
# print(obje.email)
# print(obje.telephone)
# print(obje_1.name)
# print(obje_1.surname)
# print(obje_1.password)
# print(obje_1.id_number)
# print(obje_1.email)
# print(obje_1.telephone)
#
# banka_1 = Bank()
#
# print(banka_1.login_id_password_check('12345699999', "1235"))
# print(banka_1.login_id_password_check('12345699999', "6789"))
# print(banka_1.is_avaliable('12345699999', 5000))
# print(banka_1.login_id_password_check('12345699900', "1235"))
# print(banka_1.login_id_password_check('12345699999', "6789"))
#
# banka_1.money_transfer("12345699999","12345678910",1000)


customer = Customer()

customer.new_balance(20)