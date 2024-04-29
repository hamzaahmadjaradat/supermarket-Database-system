import tkinter as tk
import mysql.connector as con
import sys

root = tk.Tk()
root.configure(background="#FFE7A0", height=200, width=200)
root.geometry("500x400")
name = tk.Label(root)
name.configure(background="#00C4FF", text='NAME')
name.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.2)
phone = tk.Label(root)
phone.configure(background="#00C4FF", text='PHONE')
phone.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.4)

email = tk.Label(root)
email.configure(background="#00C4FF", justify="left", text='EMAIL')
email.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.6)

nameEntry = tk.Entry(root)
nameEntry.configure(background="#FFF5B8")
nameEntry.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.2)

phoneEntry = tk.Entry(root)
phoneEntry.configure(background="#FFF5B8")
phoneEntry.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.4)

emailEntry = tk.Entry(root)
emailEntry.configure(background="#FFF5B8")
emailEntry.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.6)

confirmbt = tk.Button(root)
confirmbt.configure(background="#30A2FF", default="normal", state="normal", text='confirm',
                    command=lambda: add_Customer())
confirmbt.place(anchor="nw", relheight=0.1, relwidth=0.3, relx=0.4, rely=0.8)


def exit():
    root.destroy()


exitt = tk.Button(root, width=10, height=1)
exitt.configure(background="#30A2FF", default="normal", command=lambda: exit(), state="normal", text='exit')
exitt.place(x=0, y=325)


def add_Customer():
    done = tk.Label(root)
    connection = con.connect(host="localhost", user="root", password="root", database="supermarket")
    cursor = connection.cursor()
    query = "INSERT INTO customers (name,phone, email,points) VALUES ('" + nameEntry.get() + "','" + phoneEntry.get() + "','" + emailEntry.get() + "'," + "'0')"
    if nameEntry.get() == "" and phoneEntry.get() == "" and emailEntry.get() == "":
        done.configure(background="#00C4FF", text='make sure to provide all data feilds')
        done.place(x=200, y=20)
    else:
        print(query)

        cursor.execute(query)
        connection.commit()
        done.configure(background="#00C4FF", text='the customer has been added')
        done.place(x=200, y=20)
        print("the Query executed successfully!")


alarm = tk.Label(root)
alarm.configure(background="#FFE7A0")
alarm.pack(fill="x", side="top")
root.mainloop()
