from tkinter import *
from PIL import ImageTk
import sqlite3
conn=sqlite3.connect('DL.db')
print("Opened database successfully");
c = conn.cursor()

ws = Tk()

ws.geometry('10000x10000')
ws.title('PROVIDER')
ws['bg']='#ffbf00'

f = ("Times bold", 14)
c = conn.cursor()

def insertData():
    name =e1.get()
    address=e2.get()
    job_discription=e3.get()
    amount=e4.get()
    insert_query ="INSERT INTO `Homedelivery`(`name`, `address`, `job_discription`, `amount`)VALUES (?,?,?,?)"
    vals = (name,address,job_discription,amount)
    c.execute(insert_query,vals)
    conn.commit()

def provider_needer():
    ws.destroy()
    import provider_needer

def thankyou():
    ws.destroy()
    import thankyou
    
uname=Label(ws,text="Name",font=(50))
uname.place(x=450,y=150)
e1=Entry(width=30,font=(50))
e1.place(x=600,y=150)

add=Label(ws,text="Address",font=(50))
add.place(x=450,y=200)
e2=Entry(width=30,font=(50))
e2.place(x=600,y=200)

jobdesc=Label(ws,text="Job discription",font=(50))
jobdesc.place(x=450,y=250)
e3=Entry(width=30,font=(50))
e3.place(x=600,y=250)

amt=Label(ws,text="Pay Amount",font=(50))
amt.place(x=450,y=300)
e4=Entry(width=30,font=(50))
e4.place(x=600,y=300)

Button(ws,text="SAVE",background="lightgreen",command=insertData,width=15,height=2, font=(23)).place(x=660,y=420)
Button(ws,text="NEXT",background="lightgreen",command=thankyou,width=15,height=2, font=(23)).place(x=660,y=500)
Button(ws,text="BACK",background="lightblue",command=provider_needer,width=8,height=1,font=(20)).place(x=700,y=650)

ws.mainloop()