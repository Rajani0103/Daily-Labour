from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter.messagebox import showinfo
import sqlite3

ws = Tk()

ws.geometry('5000x5000')
ws.title('TYPES')
ws['bg']='#5d8a82'

f = ("Times bold", 14)

def provider_needer():
    ws.destroy()
    import provider_needer

def provider1():
    ws.destroy()
    import provider1

def provider2():
    ws.destroy()
    import provider2

def provider3():
    ws.destroy()
    import provider3

def provider4():
    ws.destroy()
    import provider4

def provider5():
    ws.destroy()
    import provider5

#def provider():
    #ws.destroy()
    #import provider

def daycare():
    ws.destroy()
    import daycare

def delivery():
    ws.destroy()
    import homedelivery

def cleaning():
    ws.destroy()
    import cleaning

def construction():
    ws.destroy()
    import construction

def driver():
    ws.destroy()
    import driver

Label(ws,text="TYPES OF JOBS",font=(25)).place(x=600,y=50)
Button(ws, text='Back',command=provider_needer,width=15,height=2,font=(20),bg='lightgreen').place(x=590,y=600)

Button(ws,text="DAY CARE",background="wheat3",command=provider1,width=25,height=1,font=(20)).place(x=550,y=300)
Button(ws,text="HOME DELIVERY",background="lightblue",command=provider2,width=25,height=1,font=(20)).place(x=550,y=100)
Button(ws,text="CLEANING",background="gainsboro",command=provider3,width=25,height=1,font=(20)).place(x=550,y=150)
Button(ws,text="CONSTRUCTION WORKING",background="thistle",command=provider4,width=25,height=1,font=(20)).place(x=550,y=200)
Button(ws,text="DRIVER",background="Peachpuff2",command=provider5,width=25,height=1,font=(20)).place( x=550,y=250)

conn = sqlite3.connect('DL.db')
print ("Opened database successfully");


conn.execute('''CREATE TABLE driver
         (name     VARCHAR    NOT NULL,
          address     VARCHAR     NOT NULL,
          job_discription   VARCHAR     NOT NULL,
          amount INT NOT NULL);
         ''')
print ("Table created successfully");
conn.close()

ws.mainloop()
