import tkinter as tk
import mysql.connector as con

def sign_up():
    root = tk.Tk()
    root.geometry('700x670')
    root.configure(bg="#404040")

    Name = tk.Label(root, text="FULL NAME", width=10, bg="#404040", font=("bold", 20), fg="#FF7F50")
    Name.place(x=270, y=30)
    entryName = tk.Entry(root, justify="center", bd=2, fg="#030303", font=("dark bold", 18))
    entryName.place(x=220, y=70)
    entryName.configure(background="#FF7F50")
    email = tk.Label(root, text="EMAIL", width=10, bg="#404040", font=("bold", 20), fg="#FF7F50")
    email.place(x=270, y=130)
    entryEmail = tk.Entry(root, justify="center", bd=2, fg="#030303", font=("dark bold", 18))
    entryEmail.place(x=220, y=170)
    entryEmail.configure(background="#FF7F50")
    password = tk.Label(root, text="PASSWORD", width=10, bg="#404040", font=("bold", 20), fg="#FF7F50")
    password.place(x=270, y=220)
    entryPassword = tk.Entry(root, justify="center", bd=2, fg="#030303", font=("dark bold", 18), show="*")
    entryPassword.place(x=220, y=260)
    entryPassword.configure(background="#FF7F50")
    phone = tk.Label(root, text="PHONE", width=10, bg="#404040", font=("bold", 20), fg="#FF7F50")
    phone.place(x=270, y=300)
    entryphone = tk.Entry(root, justify="center", bd=2, fg="#030303", font=("dark bold", 18))
    entryphone.place(x=220, y=350)
    entryphone.configure(background="#FF7F50")
    alarm = tk.Label(root, text="")

    def confirm(alarm):
        alarm.config(text="")

        if entryName.get() == "" or entryEmail.get() == "" or entryPassword.get() == "" or entryphone.get() == "":
            alarm.config(text="**make sure to enter all data right", bg="#404040", font=("bold", 20), fg="red")
            alarm.place(x=200, y=490)
        else:
            connection = con.connect(host="localhost", user="root", password="password", port="3306",
                                     database="supermarket")
            cursor = connection.cursor()
            query = "INSERT INTO customers (name, email, password, phone) VALUES (%s, %s, %s,%s)"
            values = ("" + entryName.get(), "" + entryEmail.get(), "" + entryPassword.get(), "" + entryphone.get())
            cursor.execute(query, values)
            connection.commit()
            alarm.config(text="successfully registered", bg="#404040", font=("bold", 20), fg="green")
            alarm.place(x=200, y=490)
            cursor.close()
            connection.close()

    tk.Button(root, text="confirm", cursor="hand2", command=lambda: confirm(alarm), height=-1, width=6, bg="#FF7F50",
              font=("dark bold", 22)).place(x=290, y=390)

    root.mainloop()