import mysql.connector as con
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import subprocess
import datetime
import sys

eid = int(sys.argv[1])
title = sys.argv[2]

root = tk.Tk()
root.configure(background="#116A7B", height=200, width=200)
root.geometry("900x600")
root.geometry("+100+20")

datatxt = ScrolledText(root)
datatxt.place(anchor="nw", relheight=0.6, relwidth=1.0)

sidtxt = tk.Entry(root)
sidtxt.place(anchor="nw", relwidth=0.16, relx=0.14, rely=0.7, x=0, y=0)

cidtxt = tk.Entry(root)
cidtxt.place(anchor="nw", relwidth=0.16, relx=0.45, rely=0.7, x=0, y=0)

sidlbl = tk.Label(root)
sidlbl.configure(text='saleid')
sidlbl.place(anchor="nw", relwidth=0.08, relx=0.02, rely=0.7)

cidlbl = tk.Label(root)
cidlbl.configure(text='customerid')
cidlbl.place(anchor="nw", relwidth=0.08, relx=0.34, rely=0.7)

sdatelbl = tk.Label(root)
sdatelbl.configure(text='time')
sdatelbl.place(anchor="nw", relwidth=0.08, relx=0.02, rely=0.85)

sdatetxt = tk.Entry(root)
sdatetxt.place(anchor="nw", relwidth=0.16, relx=0.14, rely=0.85)

itemsbt = tk.Button(root)
itemsbt.configure(text='show sold items')
itemsbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.84)

salesbt = tk.Button(root, command= lambda: show_sales(title, eid))
salesbt.configure(text='show sales')
salesbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.69)

if(title == 'manager'):
    eidlbl = tk.Label(root)
    eidlbl.configure(text='employeeid')
    eidlbl.place(anchor="nw", relwidth=0.08, relx=0.34, rely=0.85)

    eidtxt = tk.Entry(root)
    eidtxt.place(anchor="nw", relwidth=0.16, relx=0.45, rely=0.85)

def show_sales(title, eid):
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()

    if(title == 'manager'):
        query = "select * from sales"
        if(sidtxt.get() != ''):
            query += " where saleid = %s"
            if(cidtxt.get() != ''):
                query += " and customerid = %s"
            if(sdatetxt.get() != ''):
                query += " and time = %s"
            if(eidtxt.get() != ''):
                query += " and employeeid = %s"
            cursor.execute(query, (sidtxt.get(), cidtxt.get(), sdatetxt.get(), eidtxt.get()))

        elif(cidtxt.get() != ''):
            query += " where customerid = %s"
            if(sdatetxt.get() != ''):
                query += " and time = %s"
            if(eidtxt.get() != ''):
                query += " and employeeid = %s"
            if(sidtxt.get() != ''):
                query += " and saleid = %s"
            cursor.execute(query, (cidtxt.get(), sdatetxt.get(), eidtxt.get(), sidtxt.get()))

        elif(sdatetxt.get() != ''):
            query += " where time = %s"
            if(eidtxt.get() != ''):
                query += " and employeeid = %s"
            if(sidtxt.get() != ''):
                query += " and saleid = %s"
            if(cidtxt.get() != ''):
                query += " and customerid = %s"
            cursor.execute(query, (sdatetxt.get(), eidtxt.get(), sidtxt.get(), cidtxt.get()))

        elif(eidtxt.get() != ''):
            query += " where employeeid = %s"
            if(sidtxt.get() != ''):
                query += " and saleid = %s"
            if(cidtxt.get() != ''):
                query += " and customerid = %s"
            if(sdatetxt.get() != ''):
                query += " and time = %s"
            cursor.execute(query, (eidtxt.get(), sidtxt.get(), cidtxt.get(), sdatetxt.get()))

    else:
        query = "select * from sales where employeeid = %s"
        if(sidtxt.get() != ''):
            query += " and saleid = %s"
            cursor.execute(query, (eid, sidtxt.get(),))
        elif(cidtxt.get() != ''):
            query += " and customerid = %s"
            cursor.execute(query, (eid, cidtxt.get(),))
        elif (cidtxt.get() != '' and sdatetxt.get() != ''):
            query += " and customerid = %s and time = %s"
            cursor.execute(query, (eid, cidtxt.get(), sdatetxt.get(),))
        elif(sdatetxt.get() != ''):
            query += " and time = %s"
            cursor.execute(query, (eid, sdatetxt.get(),))
        else:
            cursor.execute(query, (eid,))

    data = cursor.fetchall()
    data2 = ""
    for row in data:
        line = " ".join(str(element) for element in row)
        data2 = "\n".join(line)
    datatxt.delete('1.0', tk.END)
    datatxt.insert('1.0', data2)
    datatxt.place(anchor="nw", relheight=0.6, relwidth=1.0)
    datatxt.configure(state='disabled')
    cursor.close()
    connection.close()

root.mainloop()