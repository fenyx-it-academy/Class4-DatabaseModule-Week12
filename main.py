# imports
import os
from tkinter import *
from PIL import Image, ImageTk
from user import User
import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://test_week13:mdb05330477@week13.ugwbo.mongodb.net/week13?retryWrites=true&w=majority")
db = client["bank"]
my_col = db["user"]

# First screen
master = Tk()
master.title('Muhammet')
master.config(bg='orange')

active_user = User(my_col)
temp_user = User(my_col)

# Functions


def show_dashboard():
    account_dashboard = Toplevel(master)
    account_dashboard.title('Dashboard')
    # Labels
    Label(account_dashboard, text="Account Dashboard", font=(
        'Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(account_dashboard, text="Welcome " + active_user.get_name(),
          font=('Calibri', 12)).grid(row=1, sticky=N, pady=5)
    # Buttons
    Button(account_dashboard, text="Personal Details", font=('Calibri', 12),
           width=30, command=personal_details).grid(row=2, sticky=N, pady=10)
    Button(account_dashboard, text="Deposit", font=('Calibri', 12),
           width=30, command=deposit).grid(row=3, sticky=N, pady=10)
    Button(account_dashboard, text="Withdraw", font=('Calibri', 12),
           width=30, command=withdraw).grid(row=4, sticky=N, pady=10)
    Button(account_dashboard, text="Transfer", font=('Calibri', 12),
           width=30, command=transfer).grid(row=5, sticky=N, pady=10)


def finish_reg():
    temp_user.set_name(temp_name.get())
    temp_user.set_age(temp_age.get())
    temp_user.set_gender(temp_gender.get())
    temp_user.set_password('', temp_password.get())

    if not temp_user.is_valid():
        notif.config(fg="red", text="All fields are required * ")
        return

    if User.user_exists(temp_user.get_name()):
        notif.config(fg="red", text="Account already exists.")
        return

    temp_user.save()
    temp_user.clear()
    notif.config(fg="green", text="Account has been opened.")


def register():
    # Variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif

    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    # Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    # Labels
    Label(register_screen, text="Please enter your details below to register.", width=50,
          bg='orange', fg='black', font=('Calibri', 10)).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text="Name:", bg='orange', fg='white',
          font=('Calibri', 12)).grid(row=1, sticky=W, padx=5, pady=5)
    Label(register_screen, text="Age:", bg='orange', fg='white',
          font=('Calibri', 12)).grid(row=2, sticky=W, padx=5, pady=5)
    Label(register_screen, text="Gender:", bg='orange', fg='white',
          font=('Calibri', 12)).grid(row=3, sticky=W, padx=5, pady=5)
    Label(register_screen, text="Password:", bg='orange', fg='white',
          font=('Calibri', 12)).grid(row=4, sticky=W, padx=5, pady=5)
    notif = Label(register_screen, font=('Calibri', 12))
    notif.grid(row=6, sticky=N, pady=10)

    # Entries
    Entry(register_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_password,
          show="*").grid(row=4, column=0)

    # Buttons
    Button(register_screen, text="Register", command=finish_reg, bg='green',
           fg='white', font=('Calibri', 12, 'bold')).grid(row=5, sticky=N, pady=10)


def login_session():
    global login_name
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    if User.user_exists(login_name, my_col):
        active_user.load(login_name)
        if active_user.check_password(login_password):
            login_screen.destroy()
            show_dashboard()
        else:
            login_notif.config(fg="red", text="Password incorrect!")
            active_user.clear()
    else:
        login_notif.config(fg="red", text="No account found!")


def deposit():
    # Variables
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()

    # Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')

    # Labels
    Label(deposit_screen, text="Deposit", font=(
        'Calibri', 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(deposit_screen, text="Current Balance : € " + str(
        active_user.get_balance()), font=('Calibri', 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(deposit_screen, text="Amount : ", font=(
        'Calibri', 12)).grid(row=2, sticky=W)
    deposit_notif = Label(deposit_screen, font=('Calibri', 12))
    deposit_notif.grid(row=4, sticky=N, pady=5)

    # Entry
    Entry(deposit_screen, textvariable=amount).grid(row=2, column=1)

    # Button
    Button(deposit_screen, text="Finish", font=('Calibri', 12),
           command=finish_deposit).grid(row=3, sticky=W, pady=5)


def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text='Amount is required!', fg="red")
    if float(amount.get()) <= 0:
        deposit_notif.config(
            text='Negative currency is not accepted!', fg="red")
        return
    active_user.deposit(int(amount.get()))
    active_user.save()

    current_balance_label.config(
        text="Current Balance : € "+str(active_user.get_balance()), fg="green")
    deposit_notif.config(text="Balance Updated", fg='green')


def withdraw():
    # Variables
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()

    # Withdraw Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Withdraw')

    # Labels
    Label(withdraw_screen, text="Withdraw", font=(
        'Calibri', 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(withdraw_screen, text="Current Balance : € "+str(
        active_user.get_balance()), font=('Calibri', 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(withdraw_screen, text="Amount : ", font=(
        'Calibri', 12)).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_screen, font=('Calibri', 12))
    withdraw_notif.grid(row=4, sticky=N, pady=5)

    # Entry
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2, column=1)

    # Button
    Button(withdraw_screen, text="Finish", font=('Calibri', 12),
           command=finish_withdraw).grid(row=3, sticky=W, pady=5)


def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text='Amount is required!', fg="red")
        return
    if int(withdraw_amount.get()) <= 0:
        withdraw_notif.config(
            text='Negative currency is not accepted!', fg="red")
        return

    if active_user.can_withdraw(int(withdraw_amount.get())):
        active_user.withdraw(int(withdraw_amount.get()))
        active_user.save()
        withdraw_notif.config(text="Balance Updated", fg='green')
        current_balance_label.config(
            text="Current Balance : € "+str(active_user.get_balance()), fg="green")
    else:
        withdraw_notif.config(text="Insufficient Funds!", fg='red')


def personal_details():
    # Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    # Labels
    Label(personal_details_screen, text="Personal Details",
          font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="Name    : " +
          active_user.get_name(), font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(personal_details_screen, text="Age     : " +
          active_user.get_age(), font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(personal_details_screen, text="Gender  : " +
          active_user.get_gender(), font=('Calibri', 12)).grid(row=3, sticky=W)
    Label(personal_details_screen, text="Balance : € " +
          str(active_user.get_balance()), font=('Calibri', 12)).grid(row=4, sticky=W)


def login():
    # Variables
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()

    # Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')

    # Labels
    Label(login_screen, text="Login to your account", font=(
        'Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(login_screen, text="Username", font=(
        'Calibri', 12)).grid(row=1, sticky=W)
    Label(login_screen, text="Password", font=(
        'Calibri', 12)).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font=('Calibri', 12))
    login_notif.grid(row=4, sticky=N)

    # Entry
    Entry(login_screen, textvariable=temp_login_name).grid(
        row=1, column=1, padx=5)
    Entry(login_screen, textvariable=temp_login_password,
          show="*").grid(row=2, column=1, padx=5)

    # Buttons
    Button(login_screen, text="Login", command=login_session, width=15,
           font=('Calibri', 12)).grid(row=3, sticky=W, pady=5, padx=5)


def transfer():
    # Variables
    global transfer_amount
    global dest_name
    global transfer_notif
    global current_balance_label
    dest_name = StringVar()
    transfer_amount = StringVar()

    # Transfer Screen
    transfer_screen = Toplevel(master)
    transfer_screen.title('Transfer')

    # Labels
    Label(transfer_screen, text="Transfer", font=(
        'Calibri', 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(transfer_screen, text="Current Balance : € " + str(
        active_user.get_balance()), font=('Calibri', 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(transfer_screen, text="Receiver : ", font=(
        'Calibri', 12)).grid(row=2, sticky=W)
    Label(transfer_screen, text="Amount : ", font=(
        'Calibri', 12)).grid(row=3, sticky=W)
    transfer_notif = Label(transfer_screen, font=('Calibri', 12))
    transfer_notif.grid(row=5, sticky=N, pady=5)

    # Entry
    Entry(transfer_screen, textvariable=dest_name).grid(row=2, column=1)
    Entry(transfer_screen, textvariable=transfer_amount).grid(row=3, column=1)

    # Button
    Button(transfer_screen, text="Finish", font=('Calibri', 12),
           command=handle_transfer).grid(row=4, sticky=W, pady=5)


def handle_transfer():
    if User.user_exists(dest_name.get()):
        temp_user.load(dest_name.get())
        if User.transfer(active_user, temp_user, int(transfer_amount.get())):
            transfer_notif.config(text='Transfer Success!', fg="green")
            current_balance_label.config(
                text="Current Balance : € " + str(active_user.get_balance()), fg="green")
        else:
            transfer_notif.config(text='Insufficient Funds!', fg="red")
    else:
        transfer_notif.config(text='Receiver not found!', fg="red")

    temp_user.clear()


# #image import
img = Image.open('image11.jpg')
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)

# Labels
Label(master, text="Refugee Bank", font=('Calibri', 14, 'bold'),
      bg='orange', fg='white').grid(row=0, sticky=N, pady=10)
Label(master, text='"The best bank application you have ever used."',
      font=('Calibri', 12, 'italic')).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

# Buttons
Button(master, text='Register', font=('Calibri', 12, 'bold'), width=20,
       bg='green', fg='white', command=register).grid(row=3, sticky=N)
Button(master, text='Login', font=('Calibri', 12, 'bold'), width=20,
       bg='green', fg='white', command=login).grid(row=4, sticky=N, pady=5)

master.mainloop()
