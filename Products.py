import tkinter as tk
import mysql.connector as con
from tkinter import ttk
import mysql.connector



root = tk.Tk()
root.title("Products")
root.geometry("900x600")
root.configure(background="gray")

style=ttk.Style()
style.theme_use("clam")
style.configure("Custom.Treeview",background="silver",rowheight=35,foreground="black",fieldbackground="silver")
style.map("Treeview",background=[("selected","blue")])
table = ttk.Treeview(root,style="Custom.Treeview")
table.pack(anchor="ne")

table.tag_configure("heading",background="red",foreground="white")

table["columns"] = ("productID", "name", "quantity", "unit", "category", "supplierID", "price")
table.column("#0",width=0)
table.column("productID", width=100)
table.column("name", width=100)
table.column("quantity", width=100)
table.column("unit", width=100)
table.column("category", width=100)
table.column("supplierID", width=100)
table.column("price",width=100)
updateInvbt = tk.Button(root,width=10, height=1)
updateInvbt.configure(background="#30A2FF", width=13, height=2,state="normal", text='Update Inventory')
updateInvbt.pack()

table.heading("#0",anchor="nw",text="")
table.heading("productID", anchor="nw",text="productID")
table.heading("name",anchor="nw", text="name")
table.heading("quantity",anchor="nw", text="quantity")
table.heading("unit",anchor="nw", text="unit")
table.heading("category",anchor="nw", text="category")
table.heading("supplierID",anchor="nw", text="supplierID",)
table.heading("price", anchor="nw", text="price")
style = ttk.Style()
style.configure("table.Heading", background="gray",)

connection = mysql.connector.connect(host="localhost", user="root",
password="root", database="supermarket")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Products")
data = cursor.fetchall()

cursor.close()
connection.close()
for item in table.get_children():
        table.delete(item)
for row in data:
        table.insert("", tk.END, values=row)


root.mainloop()
