from tkinter import *
from PIL import ImageTk
import sqlite3
conn = sqlite3.connect('DL.db')

import tkinter  as tk 
from tkinter import * 
ws=Tk()

def homedeliverydata():
    ws.destroy()
    import homedeliverydata

ws.geometry("5000x5000") 
#x =conn.execute('''SELECT * from delivery''');

cursor = conn.execute('SELECT * FROM Homedelivery')
rows = cursor.fetchall()
for i, delivery in enumerate(rows):
    for j, value in enumerate(delivery):
        label = Label(ws, text=value, font=("Arial", 12), width=25)
        label.grid(row=i, column=j, padx=10, pady=10)
    
    #button = Button(ws, text='SELECT', background='lightgreen', command=homedeliverydata, width=15, height=2)
    #button.grid(row=i, column=len(delivery), padx=10, pady=10)

# Commit changes and close the database connection
conn.commit()
conn.close()

ws.mainloop()

#i=0 # row value inside the loop 
#for delivery in x: 
    #for j in range(len(delivery)):
        #e = tk.Label(ws,text=delivery[j],font=(50),width=25) 
        #e.grid(row=i,column=j,padx=50,pady=50)
    
    #for k in range(len(delivery)+1):
            #b=Button(ws,text='SELECT',background='lightgreen',command=confirm,width=15,height=2)
            #b.grid(row=i,column=j+1,padx=50)
    #i=i+1

        
#ws.mainloop()

