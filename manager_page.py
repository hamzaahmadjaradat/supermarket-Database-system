import tkinter as tk
import mysql.connector as con
import sys
import subprocess

def open_password_change(user):
    subprocess.run(["python", "change_password.py", user])

def logout():
    root.destroy()
    subprocess.run(["python", "main.py"])

username = sys.argv[1]

root = tk.Tk()
root.configure(background="#27374D", cursor="arrow")
root.geometry('1100x670')

welcomelb = tk.Label(background="#DDE6ED", cursor="arrow", font=('bold', 20), justify="left", relief="flat", text=f'welcome {username} ')
welcomelb.place(anchor="nw", relheight=0.23, relwidth=1.0, relx=0.0, x=0, y=0)

addEmployeebt = tk.Button(background="#9DB2BF", text='Add Employee')
addEmployeebt.place(anchor="nw", relx=0.06, rely=0.33, relwidth=0.2, relheight=0.15)

addCustomerbt = tk.Button(background="#9DB2BF", text='Add Customer')
addCustomerbt.place(anchor="nw", relx=0.29, rely=0.33, relwidth=0.2, relheight=0.15)

addSalebt = tk.Button(background="#9DB2BF", text='Add Sale')
addSalebt.place(anchor="nw", relx=0.52, rely=0.33, relwidth=0.2, relheight=0.15)

addProductbt = tk.Button(background="#9DB2BF", text='Add Product')
addProductbt.place(anchor="nw", relx=0.75, rely=0.33, relwidth=0.2, relheight=0.15)
customersbt = tk.Button(background="#9DB2BF", text='Customers')
customersbt.place(anchor="nw", relx=0.29, rely=0.55, relwidth=0.2, relheight=0.15)

employeesbt = tk.Button(background="#9DB2BF", text='Employees')
employeesbt.place(anchor="nw", relx=0.52, rely=0.55, relwidth=0.2, relheight=0.15)

productsbt = tk.Button(background="#9DB2BF", text='Products')
productsbt.place(anchor="nw", relx=0.75, rely=0.55, relwidth=0.2, relheight=0.15)

changePassbt = tk.Button(root, text='change password', bg="#9DB2BF", command=lambda: open_password_change(username))
changePassbt.place(anchor="nw", relx=0.52, rely=0.77, relwidth=0.2, relheight=0.15)

logoutbt = tk.Button(root)
logoutbt.configure(background="#9DB2BF", default="normal", state="normal", text='Log Out', command=lambda: logout())
logoutbt.place(anchor="nw", relx=0.75, rely=0.77, relwidth=0.2, relheight=0.15)

root.mainloop()