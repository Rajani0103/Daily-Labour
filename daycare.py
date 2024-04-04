from tkinter import *
from PIL import ImageTk
import sqlite3
conn = sqlite3.connect('DL.db')

import tkinter  as tk 
from tkinter import * 
ws=Tk()

def daycaredata():
    ws.destroy()
    import daycaredata

ws.geometry("5000x5000") 
x=conn.execute('''SELECT * from daycare''');
i=0 # row value inside the loop 
for daycare in x: 
    for j in range(len(daycare)):
        e = tk.Label(ws,text=daycare[j],font=(50),width=25) 
        e.grid(row=i,column=j,padx=50,pady=50)
    
    for k in range(len(daycare)+1):
            b=Button(ws,text='SELECT',background='lightgreen',command=daycaredata,width=15,height=2)
            b.grid(row=i,column=j+1,padx=50)
    i=i+1

        
ws.mainloop()
