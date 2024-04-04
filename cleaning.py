from tkinter import *
from PIL import ImageTk
import sqlite3
conn = sqlite3.connect('DL.db')

import tkinter  as tk 
from tkinter import * 
ws=Tk()

def cleaningdata():
    ws.destroy()
    import cleaningdata

ws.geometry("5000x5000") 
x=conn.execute('''SELECT * from cleaning''');
i=0 # row value inside the loop 
for cleaning in x: 
    for j in range(len(cleaning)):
        e = tk.Label(ws,text=cleaning[j],font=(50),width=25) 
        e.grid(row=i,column=j,padx=50,pady=50)
    
    for k in range(len(cleaning)+1):
            b=Button(ws,text='SELECT',background='lightgreen',command=cleaningdata,width=15,height=2)
            b.grid(row=i,column=j+1,padx=50)
    i=i+1



ws.mainloop()

