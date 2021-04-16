


from pymongo import MongoClient
import tkinter as tk

root = tk.Tk()
root.title("Customer Information Database")
root.geometry("600x400")

name_var = tk.StringVar()
surname_var = tk.StringVar()
age_var= tk.IntVar()
id_var= tk.IntVar()

def submit():
    name = name_var.get()
    surname = surname_var.get()
    age = age_var.get()
    id = id_var.get()

    cluster = MongoClient("mongodb+srv://Mahir:Denizli20@cluster0.pnlce.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster["Mahir"]
    collection = db["test"]
    post = {"_id": id, "name": name, "surname": surname, "age": age}
    collection.insert_one(post)

    name_var.set("")
    surname_var.set("")
    age_var.set("")
    id_var.set("")

def delete():
    # name = name_var.get()
    # surname = surname_var.get()
    # age = age_var.get()
    id= id_var.get()

    cluster = MongoClient("mongodb+srv://Mahir:Denizli20@cluster0.pnlce.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster["Mahir"]
    collection = db["test"]
    post1 = {"_id": id}
    collection.delete_one(post1)

    # name_var.set("")
    # surname_var.set("")
    # age_var.set()
    id_var.set("")

name_label = tk.Label(root, text='Name', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

id_label = tk.Label(root, text='ID', font=('calibre', 10, 'bold'))
id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal'))

age_label = tk.Label(root, text='Age', font=('calibre', 10, 'bold'))
age_entry = tk.Entry(root, textvariable=age_var, font=('calibre', 10, 'normal'))

surname_label = tk.Label(root, text='Surname', font=('calibre', 10, 'bold'))
surname_entry = tk.Entry(root, textvariable=surname_var, font=('calibre', 10, 'normal'), show='*')


sub_btn = tk.Button(root, text='Add', command=submit)
sub_btn2 = tk.Button(root, text='Delete', command=delete)

id_label.grid(row=0, column=0)
id_entry.grid(row=0, column=1)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
age_label.grid(row=3, column=0)
age_entry.grid(row=3, column=1)
surname_label.grid(row=2, column=0)
surname_entry.grid(row=2, column=1)
sub_btn.grid(row=4, column=1)
sub_btn2.grid(row=4, column=2)

root.mainloop()
