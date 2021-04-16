from tkinter import *
from tkinter import messagebox
from random import randint
import os
from PIL import Image, ImageTk
import re

from Account import Account
from User import User


class UI_Class(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.user = User()
        self.account = Account()

        self.master.geometry("500x500")
        self.master.title("Most Secure banking")
        self.master.geometry("500x500")
        self.master.config(bg='orange')
        # pages
        self.entry_page = Frame(self.master)
        self.user_create_page = Frame(self.master)
        self.user_logged_page = Frame(self.master)
        self.user_login_page = Frame(self.master)

        self.user_deposit_page = Frame(self.master)
        self.user_withdraw_page = Frame(self.master)
        self.user_edit_page = Frame(self.master)
        self.user_delete_page = Frame(self.master)
        self.user_send_page = Frame(self.master)
        self.user_overview_page = Frame(self.master)

        self.UI_elements()
        self.create_entry_page()
        self.open_windows = []

    # Pages
    def create_entry_page(self):

        self.entry_page.config(bg='orange')
        self.entry_page.grid(row=0)
        self.entry_logo_label.grid(row=0, sticky=N, pady=10)
        self.entry_logo_label_2.grid(row=1, sticky=N)

        self.entry_create_button.grid(row=3, pady=10)
        self.entry_login_button.grid(row=4,  pady=10)
        self.entry_exit_button.grid(row=5,  pady=10)

    def create_page(self):
        self.entry_page.grid_remove()
        self.user_create_page.config(bg='orange')

        self.user_create_page.grid(row=0)
        self.create_label_1.grid(row=0, column=0)
        self.create_entry_1.grid(row=0, column=1)

        self.create_label_2.grid(row=1, column=0)
        self.create_entry_2.grid(row=1, column=1)

        self.create_label_3.grid(row=2, column=0)
        self.create_entry_3.grid(row=2, column=1)

        self.create_submit_button.grid(row=3, sticky=W)
        self.create_home_button.grid(row=4, sticky=W)

    def login_page(self):
        self.entry_page.grid_remove()
        self.user_login_page.config(bg='orange')

        self.user_login_page.grid(row=0)

        self.login_label_1.grid(row=0, column=0)
        self.login_entry_1.grid(row=0, column=1)

        self.login_label_2.grid(row=1, column=0)
        self.login_entry_2.grid(row=1, column=1)

        self.login_label_3.grid(row=2, column=0)
        self.login_entry_3.grid(row=2, column=1)

        self.login_submit_button.grid(row=3)
        self.login_home_button.grid(row=4)

    def logged_page(self):
        self.user_login_page.grid_remove()
        self.user_create_page.grid_remove()
        self.user_logged_page.config(bg='orange')

        self.user_logged_page.grid(row=0)

        self.logged_deposit_button.grid(row=0)
        self.logged_withdraw_button.grid(row=1)
        self.logged_send_money_button.grid(row=2)
        self.logged_overview_button.grid(row=3)
        self.logged_edit_personal_detail.grid(row=4)
        self.logged_delete_button.grid(row=5)
        self.logged_logout_button.grid(row=6)

    def withdraw_page(self):
        self.user_logged_page.grid_remove()
        self.user_withdraw_page.config(bg='orange')

        self.user_withdraw_page.grid(row=0)
        self.withdraw_label_1.grid(row=0, column=0)
        self.withdraw_entry_1.grid(row=0, column=1)

        self.withdraw_submit_button.grid(row=1)
        self.withdraw_home_button.grid(row=2)

    def deposit_page(self):
        self.user_logged_page.grid_remove()
        self.user_deposit_page.config(bg='orange')

        self.user_deposit_page.grid(row=0)
        self.deposit_label_1.grid(row=0, column=0)
        self.deposit_entry_1.grid(row=0, column=1)

        self.deposit_submit_button.grid(row=1)
        self.deposit_home_button.grid(row=2)

    def edit_personal_page(self):
        self.user_logged_page.grid_forget()
        self.user_edit_page.config(bg='orange')

        self.user_edit_page.grid(row=0)
        self.edit_label_1.grid(row=0, column=0)
        self.edit_entry_1.grid(row=0, column=1)

        self.edit_label_2.grid(row=1, column=0)
        self.edit_entry_2.grid(row=1, column=1)

        self.edit_submit_button.grid(row=2)
        self.edit_home_button.grid(row=3)

    def overview_page(self):
        self.user_logged_page.grid_remove()
        self.user_overview_page.config(bg='orange')

        self.user_overview_page.grid(row=0)
        name = 'Account Holder Name:   ' + self.user.name
        acc_num = 'Account Number:   ' + self.user.account_num
        balance = 'Your Balance:    ' + str(self.user.balance)
        self.overview_label_1.config(text=name)
        self.overview_label_1.grid(row=0, sticky=W)

        self.overview_label_2.config(text=acc_num)
        self.overview_label_2.grid(row=1, sticky=W)

        self.overview_label_3.config(text=balance)
        self.overview_label_3.grid(row=2, sticky=W)
        self.overview_home_button.grid(row=3, sticky=W)

    def delete_page(self):
        self.user_logged_page.grid_remove()
        self.user_delete_page.config(bg='orange')

        self.user_delete_page.grid(row=0)

        self.delete_entry_1.grid(row=0)
        self.delete_yes_button.grid(row=1, column=0)
        self.delete_no_button.grid(row=1, column=1)

    def send_page(self):
        self.user_logged_page.grid_remove()
        self.user_send_page.config(bg='orange')

        self.user_send_page.grid(row=0)

        self.send_label_1.grid(row=0, column=0)
        self.send_entry_1.grid(row=0, column=1)

        self.send_label_2.grid(row=1, column=0)
        self.send_entry_2.grid(row=1, column=1)

        self.send_submit_button.grid(row=2)
        self.send_home_button.grid(row=3)

    ###Submit buttons ####

    def check_create_user(self):
        if self.check__number(self.create_entry_2.get()):
            user_name = self.create_entry_1.get()
            user_balance = int(self.create_entry_2.get())
            user_pin = self.create_entry_3.get()

            if user_pin == '' or user_name == '' or user_balance == '':
                messagebox.showwarning(
                    "Try Again", "You have to enter all of the information!!!")
            else:
                result = self.user.create_user(
                    user_name, user_balance, user_pin)
                if result:
                    messagebox.showinfo('Operation is successful!',
                                        'Successfully created an account, \n Your account number is ' + str(self.user.account_num)+' please login to the system')

                    self.login_page()
        else:
            messagebox.showinfo("", 'Balance must be a number')

    def login(self):
        user_name = self.login_entry_1.get()
        user_account = int(self.login_entry_2.get())
        user_pin = self.login_entry_3.get()

        if user_name == '' or user_account == '' or user_pin == '':
            messagebox.showwarning(
                'Invalid way of Entering', 'You need to enter all of the information')
        else:
            return_result = self.user.login(user_name, user_account, user_pin)

            if return_result == True:

                self.account.login(
                    self.user.name, self.user.balance, self.user.account_num)

                self.logged_page()
            elif return_result == False:
                messagebox.showwarning(
                    "Operation is not successful", 'Cannot find user')
            elif return_result == "Informations entered doesn't match":
                messagebox.showwarning(
                    'Not valid data', 'Your informations are not correct')

    def deposit(self):
        if self.check__number(self.deposit_entry_1.get()):
            amount = int(self.deposit_entry_1.get())
            result_user = self.user.update_balance(
                'deposit', self.user.account_num, amount)
            if result_user:
                result_account = self.account.deposit_money(amount)

            if result_account:
                messagebox.showinfo(
                    "Success", 'Operation is succesfully done.')
            self.return_logged_menu(self.user_deposit_page)
        else:
            messagebox.showerror('', 'Amount must be integer')

    def widthdraw(self):
        if self.check__number(self.withdraw_entry_1.get()):
            amount = int(self.withdraw_entry_1.get())
            result_user = self.user.update_balance(
                'withdraw', self.user.account_num, amount)
            if result_user:
                result_account = self.account.withdraw_money(amount)

            if result_account:
                messagebox.showinfo(
                    "Success", 'Operation is succesfully done.')

            self.return_logged_menu(self.user_withdraw_page)
        else:
            messagebox.showerror('', 'Amount must be integer')

    def send_submit(self):
        if self.check__number(self.send_entry_2.get()):

            to_acc_num = int(self.send_entry_1.get())
            amount = int(self.send_entry_2.get())
            return_result = self.user.send_money(to_acc_num, amount)
            if return_result > 0:
                result_account = self.account.send_money(
                    to_acc_num, amount, return_result)
            if result_account:
                messagebox.showinfo(
                    "Success", 'Operation is succesfully done.')
            else:
                messagebox.showinfo("", 'insufficient balance')
            self.return_logged_menu(self.user_send_page)
        else:
            messagebox.showerror('', 'Amount must be integer')

    def return_home(self):
        self.user.name = ''
        self.user.pin = ''
        self.user.account_num = ''
        self.user_logged_page.grid_remove()
        self.user_login_page.grid_remove()
        self.user_create_page.grid_remove()
        self.create_entry_page()

    def edit_info(self):
        name = self.edit_entry_1.get()
        pin = self.edit_entry_2.get()
        self.user.update_info(name, pin)
        self.logged_page()

    def delete_account(self):
        self.user.remove_account()
        self.account.remove_account()
        self.user.name = ''
        self.user.account_num = ''
        self.user.balance = ''
        self.user.pin = ''
        self.create_entry_page()
    #### Cancel Buttons #####

    def return_logged_menu(self, page):
        page.grid_remove()
        self.logged_page()

    def exit_pages(self):
        self.master.destroy()

    ###### UTILITIES ######
    def check__number(self, entry):
        try:
            float(entry)
            return 1
        except ValueError:
            return 0

    #### UI ELEMENTS #####

    def UI_elements(self):
        # Entry Pages
        self.entry_logo_label = Label(self.entry_page, text="Refugee Bank", font=(
            'Calibri', 14, 'bold'), bg='orange', fg='white')
        self.entry_logo_label_2 = Label(
            self.entry_page, text='"The best bank application you have ever used."', font=('Calibri', 12, 'italic'))

        self.entry_create_button = Button(
            self.entry_page, text='Register', font=('Calibri', 12, 'bold'), width=20, bg='blue', fg='white',  command=self.create_page)
        self.entry_login_button = Button(
            self.entry_page, text='Login', font=('Calibri', 12, 'bold'), width=20, bg='blue', fg='white', command=self.login_page)
        self.entry_exit_button = Button(
            self.entry_page, text='Exit', font=('Calibri', 12, 'bold'), width=20, bg='blue', fg='white', command=self.exit_pages)

        ###### CREATE PAGE ######
        # Labels
        self.create_label_1 = Label(
            self.user_create_page, text='Enter Name: ')
        self.create_label_2 = Label(
            self.user_create_page, text='Enter deposit amount: ')
        self.create_label_3 = Label(
            self.user_create_page, text='Enter desired PIN: ')

        # Entry
        self.create_entry_1 = Entry(self.user_create_page)
        self.create_entry_2 = Entry(self.user_create_page)
        self.create_entry_3 = Entry(self.user_create_page, show='*')

        # Buttons
        self.create_submit_button = Button(
            self.user_create_page, text="Submit", command=self.check_create_user)

        self.create_home_button = Button(self.user_create_page,
                                         text="Cancel", command=self.return_home)

        ###### LOGIN PAGE ######
        # Lables
        self.login_label_1 = Label(self.user_login_page,
                                   text='Enter your name: ')
        self.login_label_2 = Label(self.user_login_page,
                                   text='Enter account number: ')
        self.login_label_3 = Label(self.user_login_page,
                                   text='Enter your PIN: ')

        # Entry
        self.login_entry_1 = Entry(self.user_login_page)
        self.login_entry_2 = Entry(self.user_login_page)
        self.login_entry_3 = Entry(self.user_login_page, show='*')

        # Buttons
        self.login_submit_button = Button(
            self.user_login_page, text="Submit", command=self.login)

        self.login_home_button = Button(self.user_login_page,
                                        text="Cancel", command=self.return_home)

        ###### LOGGED PAGE ######
        # Buttons
        self.logged_withdraw_button = Button(self.user_logged_page,
                                             text="Withdraw Money", command=self.withdraw_page)
        self.logged_deposit_button = Button(self.user_logged_page,
                                            text="Deposit Money", command=self.deposit_page)
        self.logged_edit_personal_detail = Button(self.user_logged_page,
                                                  text="Edit Personal Detail", command=self.edit_personal_page)
        self.logged_delete_button = Button(self.user_logged_page,
                                           text="Delete account", command=self.delete_page)

        self.logged_send_money_button = Button(self.user_logged_page,
                                               text="Send money", command=self.send_page)
        self.logged_overview_button = Button(self.user_logged_page,
                                             text="Overview your account", command=self.overview_page)
        self.logged_logout_button = Button(self.user_logged_page,
                                           text="Logout", command=self.return_home)

        ###### DEPOSIT  PAGE ######
        # Lables
        self.deposit_label_1 = Label(self.user_deposit_page,
                                     text='Enter the amount: ')

        # Entry
        self.deposit_entry_1 = Entry(
            self.user_deposit_page, text=self.user.name)

        # Buttons
        self.deposit_submit_button = Button(
            self.user_deposit_page, text="Submit", command=self.deposit)

        self.deposit_home_button = Button(self.user_deposit_page,
                                          text="Cancel", command=lambda: self.return_logged_menu(self.user_deposit_page))

        ###### Withdraw  PAGE ######
        # Lables
        self.withdraw_label_1 = Label(self.user_withdraw_page,
                                      text='Enter the amount: ')

        # Entry
        self.withdraw_entry_1 = Entry(
            self.user_withdraw_page, text=self.user.name)

        # Buttons
        self.withdraw_submit_button = Button(
            self.user_withdraw_page, text="Submit", command=self.widthdraw)

        self.withdraw_home_button = Button(self.user_withdraw_page,
                                           text="Cancel", command=lambda: self.return_logged_menu(self.user_withdraw_page))

        ###### SEND MONEY PAGE ######
        # Lables
        self.send_label_1 = Label(self.user_send_page,
                                  text='Enter the reciever account number: ')
        self.send_label_2 = Label(self.user_send_page,
                                  text='Enter the amount: ')

        # Entry
        self.send_entry_1 = Entry(self.user_send_page)
        self.send_entry_2 = Entry(self.user_send_page)

        # Buttons
        self.send_submit_button = Button(
            self.user_send_page, text="Submit", command=self.send_submit)

        self.send_home_button = Button(self.user_send_page,
                                       text="Cancel", command=lambda: self.return_logged_menu(self.user_send_page))

        ###### EDIT PERSONAL DETAIL PAGE ######
        # Lables
        self.edit_label_1 = Label(self.user_edit_page,
                                  text='Enter your name: ')
        self.edit_label_2 = Label(self.user_edit_page,
                                  text='Enter your PIN: ')

        # Entry
        self.edit_entry_1 = Entry(self.user_edit_page, text=self.user.name)
        self.edit_entry_2 = Entry(self.user_edit_page, show='*')

        # Buttons
        self.edit_submit_button = Button(
            self.user_edit_page, text="Submit", command=self.edit_info)

        self.edit_home_button = Button(self.user_edit_page,
                                       text="Cancel", command=lambda: self.return_logged_menu(self.user_edit_page))
        ####### OVERVIEW PAGE ######
        # Labels
        self.overview_label_1 = Label(self.user_overview_page,
                                      text='Account Holder Name: '+self.user.name)
        self.overview_label_2 = Label(self.user_overview_page,
                                      text='Account Number: '+str(self.user.account_num))
        self.overview_label_3 = Label(self.user_overview_page,
                                      text='Your Balance: '+self.user.balance)

        # Button
        self.overview_home_button = Button(self.user_overview_page,
                                           text="Return", command=lambda: self.return_logged_menu(self.user_overview_page))

        ###### DELETE PAGE ######
        # Labels
        self.delete_entry_1 = Label(
            self.user_delete_page, text='Would you like to delete your account? \nThink about it again!!!!')

        # Buttons
        self.delete_yes_button = Button(
            self.user_delete_page, text='YES', command=self.delete_account)
        self.delete_no_button = Button(
            self.user_delete_page, text="No", command=lambda: self.return_logged_menu(self.user_delete_page))


root = Tk()
app = UI_Class(root)
app.mainloop()
