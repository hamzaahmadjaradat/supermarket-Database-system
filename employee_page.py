import tkinter as tk
import mysql.connector as con
import sys
import subprocess

def open_password_change(user):
    subprocess.run(["python", "change_password.py", user])
def open_add_customer():
    print("rgrewg")
    subprocess.run(["python", "add_customer.py"])
def add_sale():
    print("saleeee"+str(eid))
    subprocess.run(["python", "add_sale.py",str(eid)])


def logout():
    root.destroy()
    subprocess.run(["python", "main.py"])

def open_sales(eid, title):
    root.destroy()
    subprocess.run(["python", "sales.py", str(eid), title])
def open_Products():
    subprocess.run(["python", "Products.py"])
def printBill():
    subprocess.run(["python", "Bill.py"])

username = sys.argv[1]
title = sys.argv[2]
eid = int(sys.argv[3])

root = tk.Tk()
root.configure(background="#0A4D68")
root.geometry("900x600")
root.geometry("+100+20")


welcomelb = tk.Label(root)
welcomelb.configure(background="#088395", font=('bold', 20), text=f'welcome {username} ')
welcomelb.place(anchor="nw", relheight=0.2, relwidth=1.0)

addCustomerbt = tk.Button(root)
addCustomerbt.configure(background="#00FFCA", cursor="arrow",command =lambda:open_add_customer(), default="normal", text='Add Customer')
addCustomerbt.place(relheight=0.15, relwidth=0.2, relx=0.1, rely=0.25)

addSalebt = tk.Button(root)
addSalebt.configure(background="#00FFCA",command = lambda : add_sale(), text='Add Sale')
addSalebt.place(relheight=0.15, relwidth=0.2, relx=0.4, rely=0.25)

salebt = tk.Button(root, command= lambda: open_sales(eid, title))
salebt.configure(background="#00FFCA", text='Sales')
salebt.place(relheight=0.15, relwidth=0.2, relx=0.7, rely=0.25)

changePassbt = tk.Button(root)
changePassbt.configure(background="#00FFCA", default="normal", state="normal", text='change password', command=lambda: open_password_change(username))
changePassbt.place(relheight=0.15, relwidth=0.2, relx=0.1, rely=0.49)


Products = tk.Button(root)
Products.configure(background="#00FFCA", text='Products', command= lambda: open_Products())
Products.place(relheight=0.15, relwidth=0.2, relx=0.4, rely=0.49)

logoutbt = tk.Button(root)
logoutbt.configure(background="#00FFCA", default="normal", state="normal", text='Log Out', command=lambda: logout())
logoutbt.place(relheight=0.15, relwidth=0.2, relx=0.7, rely=0.49)

bill = tk.Button(root)
bill.configure(background="#00FFCA", default="normal", state="normal", text='BILL', command=lambda: printBill())
bill.place(relheight=0.15, relwidth=0.2, relx=0.1, rely=0.7)


root.mainloop()