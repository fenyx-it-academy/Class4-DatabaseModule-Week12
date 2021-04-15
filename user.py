import os

class User():
    def __init__(self, col):
        self.clear()
        self.col = col

    def save(self):
        user = self.col.insert_one({"name": self.name, "password": self.password, "age": self.age, "gender": self.gender, "balance": self.balance })
        # print(user)
        # new_file = open(self.name,"w")
        # new_file.write(self.name+'\n')
        # new_file.write(self.password+'\n')
        # new_file.write(self.age+'\n')
        # new_file.write(self.gender+'\n')
        # new_file.write(str(self.balance))
        # new_file.close()

    def load(self, name):
        user = self.col.find_one({"name": name})
        self.name = user["name"]
        self.password = user["password"]
        self.age = user["age"]
        self.gender = user["gender"]
        self.balance = int(user["balance"])
        # file = open(name,"r")
        # file_data = file.read()
        # file_data = file_data.split('\n')
        # self.name = file_data[0]
        # self.password = file_data[1]
        # self.age = file_data[2]
        # self.gender = file_data[3]
        # self.balance = int(file_data[4])

    def is_valid(self):
        return not (self.name == "" or self.age == "" or self.gender == "" or self.password == "")

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def can_withdraw(self, amount):
        return self.balance >= amount
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
    
    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_balance(self):
        return self.balance

    def set_password(self, old_password, new_password):
        if(self.check_password(old_password)):
            self.password = new_password
            return True
        else:
            return False

    def check_password(self, password):
        return self.password == password

    def clear(self):
        self.age = ''
        self.gender = ''
        self.name = ''
        self.balance = 0
        self.password = ''

    @staticmethod
    def user_exists(name, col):
        user = col.find_one({"name": name})
        if(user == None ):
            return False
        else:
            return True
        # all_accounts = os.listdir()
        # for account in all_accounts:
        #     if name == account:
        #         return True
        # return False

    @staticmethod
    def transfer(source, dest, amount):
        if source.can_withdraw(amount):
            source.withdraw(amount)
            dest.deposit(amount)
            source.save()
            dest.save()
            return True
        else:
            return False

    