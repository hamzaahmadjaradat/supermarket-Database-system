import tkinter as tk
from tkinter import ttk
import mysql.connector as con
import sys
from queue import Queue
from tkinter import font
import subprocess
root = tk.Tk()
root.configure(background="#FFE7A0", height=200, width=200)
root.geometry("800x500")
total=0
combo = ttk.Combobox(root)
saleID = sys.argv[1]
text_area = tk.Text(root, width=70, height=10)
text_area.place(x=200,y=130)
text_area.configure(background="#FFE7A0")

# Insert text into the text area
text_area.insert(tk.END, "solditemID            PRODUCT_NAME          QUANTITY          PRICE")
queue = Queue()
def add_product():
     combo.place(x=-1000, y=-1000)
     done = tk.Label(root)
     if nameEntry.get()=="" and quantityEntry.get()=="":
        done.configure(background="#00C4FF", text='make sure to provide all data feilds')
        done.place(x=70, y=280)

     else:
         connection = con.connect(host="localhost", user="root", password="root", database="supermarket")
         cursor = connection.cursor()
         query = "select price, quantity,productID from products where name ='" + str(nameEntry.get()) + "'"
         cursor.execute(query)
         data = cursor.fetchall()
         priceReal=int(data[0][0])
         productID = data[0][2]
         quantityReal=int(data[0][1])
         price = priceReal * int(quantityEntry.get())

         if quantityReal<int(quantityEntry.get()) :
             done.configure(text="there is no enough quantity" ,font=("Arial", 18))
             done.place(x=70, y=310)
         else:
            connection = con.connect(host="localhost", user="root", password="root", database="supermarket")
            cursor = connection.cursor()
            quantityReal=quantityReal-int(quantityEntry.get())
            query = "UPDATE products SET quantity = "+ str(quantityReal)+" WHERE name ='"+str(nameEntry.get())+"'"
            cursor.execute(query)
            connection.commit()
            cursor.close()
            connection.close()

            connection = con.connect(host="localhost", user="root", password="root", database="supermarket")
            cursor = connection.cursor()
            query = "INSERT INTO solditem (productID,productName,saleID, quantity,price) VALUES ('" +str(productID) +"','"+nameEntry.get()+"','"+str(saleID)+"'," + "'"+quantityEntry.get()+"','"+str(price)+"')"
            cursor.execute(query)
            connection.commit()
            cursor.close()
            connection.close()
            connection = con.connect(host="localhost", user="root", password="root", database="supermarket")
            cursor = connection.cursor()
            query = "select sum(price)from solditem where saleID=" + str(saleID)
            cursor.execute(query)
            data = cursor.fetchall()
            total = data[0][0]
            connection.commit()
            cursor.close()
            connection.close()

            connection = con.connect(host="localhost", user="root", password="root", database="supermarket")
            cursor = connection.cursor()
            query = "select max(solditemID)from solditem "
            cursor.execute(query)
            data = cursor.fetchall()
            soldID = data[0][0]
            connection.commit()
            cursor.close()
            connection.close()
            textString= "\n"+str(soldID)+"          "+nameEntry.get()+"          "+""+quantityEntry.get()+"           "+""+str(price)
            queue.put(textString)
            text_area.insert(tk.END,"\n"+str(soldID)+"\t\t\t"+nameEntry.get()+"\t\t\t"+""+quantityEntry.get()+"\t\t"+""+str(price))

            nameEntry.delete(0, tk.END)
            quantityEntry.delete(0, tk.END)

fontt = font.Font(size=20)
name = tk.Label(root)
name.configure(background="#00C4FF",width=20, height=2, text='NAME')
name.place(x=70,y=20)
quantity = tk.Label(root)
quantity.configure(background="#00C4FF",width=20, height=2, text='QUANTITY')
quantity.place(x=70,y=80)



nameEntry = tk.Entry(root)
nameEntry.configure(background="#FFF5B8", font=fontt)
nameEntry.place(x=200,y=20)

quantityEntry = tk.Entry(root)
quantityEntry.configure(background="#FFF5B8", font=fontt)
quantityEntry.place(x=200,y=80)


confirmbt = tk.Button(root)
confirmbt.configure(background="#30A2FF", width=13, height=2, default="normal", state="normal", text='confirm', command= lambda: add_product())
confirmbt.place(x=70,y=130)


def remove_single_product(event):
    text = combo.get()
    text2=text
    combo.delete(combo['values'].index(text))
    deletedSoldID = text.split()[0]
    connection = con.connect(host="localhost", user="root", password="root", database="supermarket")
    cursor = connection.cursor()
    query = "delete from solditem where solditemID ="+deletedSoldID
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

    connection = con.connect(host="localhost", user="root", password="root", database="supermarket")
    cursor = connection.cursor()
    query = "select solditemID,productName ,quantity,price from solditem where saleID ="+saleID
    cursor.execute(query)
    buildTextArea=cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

    text_area.delete("1.0", "end")
    text_area.insert(tk.END, "solditemID            PRODUCT_NAME          QUANTITY          PRICE")
    combo['values'] = ()
    queue2 = Queue()
    for row in buildTextArea:
        text_area.insert(tk.END, "\n"+""+str(row[0])+"\t\t\t"+row[1]+"\t\t\t"+str(row[2])+"\t\t"+str(row[3]))
        item=""+str(row[0])+"   "+" "+row[1]+"    "+str(row[2])+"   "+str(row[3])
        queue2.put(item)
    while not queue.empty():
        queue.get()

    combo['values'] = list(queue2.queue)
    while not queue2.empty():
        queue.put(queue2.get())



def remove_product():
    combo.place(x=70,y=320,width=350,height=30)
    combo['values'] = list(queue.queue)
    combo.bind("<<ComboboxSelected>>", remove_single_product)




remove = tk.Button(root)
remove.configure(background="#30A2FF", width=13, height=2, default="normal", state="normal", text='remove product', command= lambda: remove_product())
remove.place(x=70,y=180)




def exit():
    connection = con.connect(host="localhost", user="root", password="root", database="supermarket")
    cursor = connection.cursor()
    query2 = query = "UPDATE sales SET total = "+ str(total)+" WHERE saleID ="+str(saleID)
    cursor.execute(query2)
    connection.commit()
    cursor.close()
    connection.close()
    root.destroy()
exitt = tk.Button(root,width=10, height=1)
exitt.configure(background="#30A2FF", width=13, height=2, default="normal",command= lambda: exit(), state="normal", text='exit')
exitt.place(x=70,y=230)

alarm = tk.Label(root)
alarm.configure(background="#FFE7A0")
alarm.pack(fill="x", side="top")
root.mainloop()