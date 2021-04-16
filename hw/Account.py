from time import gmtime, strftime
import os


class Account:

    def __init__(self):
        self.name = ''
        self.balance = ''
        self.account_number = ''

    def login(self, name, balance, account_num):
        self.name = name
        self.balance = balance
        self.account_number = account_num

    def init_account(self, name, balance, acc_num):
        self.name = name
        self.balance = balance
        self.account_number = acc_num
        with open(str(acc_num)+'-rec.txt', "w") as frec:
            frec.write(
                "Date\t\t\t\t\t\t\t\tDeposit\t\t\twithdraw\t\t\t\tBalance\n")
            frec.write(str(strftime("[%Y-%m-%d] [%H-%M-%S]", gmtime())
                           )+"\t\t\t\t"+str(balance)+'\t\t\t\t\t\t\t\t\t\t'+str(balance))

 

    def deposit_money(self, amount):
        self.balance = int(self.balance) + amount
        self.add_line_to_file(
            amount, 'deposit', self.account_number, self.balance)
        return True

    def withdraw_money(self, amount):
        if int(self.balance) - amount < 0:
            return False
        self.balance = int(self.balance) - amount
        self.add_line_to_file(str(amount), 'withdraw',
                              str(self.account_number), self.balance)

    def account_overview(self):
        with open(str(self.account_number)+'-rec.txt', 'r') as f:
            return f.readlines()

    def send_money(self, to_acc_num, amount, balance):
        if int(self.balance) - int(amount) > 0:
            self.add_line_to_file(amount, 'deposit', to_acc_num, balance)
            self.add_line_to_file(amount, 'withdraw',
                                  self.account_number, self.balance)
            return True
        else:
            return False

    def remove_account(self):
        os.remove(self.account_number+'-rec.txt')

    def add_line_to_file(self, amount, operation_type, acc_num, balance):

        if operation_type == 'deposit':
            line = '\n'+str(strftime("[%Y-%m-%d] [%H-%M-%S]", gmtime())
                            )+"\t\t\t\t"+str(amount)+'\t\t\t\t\t\t\t\t\t\t'+str(balance)
        elif operation_type == 'withdraw':
            line = '\n'+str(strftime("[%Y-%m-%d] [%H-%M-%S]", gmtime())
                            )+"\t\t\t\t\t\t\t\t"+str(amount) + "\t\t\t\t\t\t" + str(balance)

        all_accounts = os.listdir()
        filename = acc_num + '-rec'
        for file in all_accounts:
            if filename in file:
                with open(file, 'a') as f:

                    f.write(line)

    def save_file(self):
        pass
