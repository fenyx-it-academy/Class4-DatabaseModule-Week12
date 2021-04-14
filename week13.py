from pymongo import MongoClient
from datetime import datetime
connect=MongoClient('mongodb+srv://emrah:2520@cluster0.f2kvo.mongodb.net/pycoder?retryWrites=true&w=majority')
db=connect['week13']
collection=db['pycoder']

class Customer: 
      
    def __init__(self,id=None,name=None,surname=None,customerid=None,telephone=None):
        self.id=id
        self.name=name 
        self.surname=surname
        self.customerid=customerid
        self.telephone=telephone
        self.date=f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'   


    def find_customer_information(self): #show all customer informations
        list=[]
        for x in collection.find():
            if x:
                for a,b in x.items():
                    if a !="Transactions":
                        list.append(a)
                        list.append(b)
                return (list)
        
        
            
    def customer_change_information(self):      #change customer infrmations
        collection.update_one({"_id":self.id},{'$set':{'name':self.name}})
        return f'{self.date} {"your information updated..."}'
    
    def balance_information(self):  #show only customer balance 
        return collection.find_one({"customerid":self.customerid})['balance']        
    
class Transactions(Customer):

    def __init__(self,id,name,surname,customerid,telephone,add_money,withdraw_money):
        super().__init__(id,name,surname,customerid,telephone)

        self.add_money=add_money
        self.withdraw_money=withdraw_money      
        
    def find_customer_transactions(self):
        for x in collection.find():
            return f" Transactions: {x['Transactions']}"
        
    def customer_money_transactions(self): #add of withdraw money  
        if self.add_money is not None: 
                           
            return (self.add_money)+(self.balance_information()) 
                
        return (self.balance_information())-(self.withdraw_money)
        
    
    def update_balance(self): #update balance
        collection.update_one({"_id":self.id},{'$set':{'balance':self.customer_money_transactions()}})
        return f'new balance:{self.balance_information()}'
        
    def insert_transactions(self): #add of withdraw money inserted 
        if self.add_money is not None:
            collection.update_one({"_id":self.id},{'$push':{"Transactions":f'{self.date} +{self.add_money}'}})
        else:    
            collection.update_one({"_id":self.id},{'$push':{f"Transaction":f'{self.date} +{self.withdraw_money}'}})
        



user=Transactions(1,'Emrah','YILDIRIM','123456789','66665555',500,None)



# print(user.customer_change_information())
# print(user.find_customer_information())

# print(user.customer_money_transactions())
# user.update_balance()
# user.insert_transactions()
print(user.find_customer_transactions())
