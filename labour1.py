from tkinter import *
from PIL import ImageTk

ws = Tk()
# img= PhotoImage(file='start.jpg',master= ws)



ws.geometry('10000x10000')
ws.title('Starts')
ws['bg']='Cadetblue4'

f = ("Times bold", 14)

def login():
    ws.destroy()
    import login

def register():
    ws.destroy()
    import register
    
Label(ws,text="START",font=(10)).pack()
Button(ws,text="LOGIN",background="azure2",command=login,width=24,height=4,font=(30)).place(x=450,y=500)
Button(ws,text="REGISTER",background="azure2",command=register,width=24,height=4,font=(30)).place(x=800,y=500)

ws.mainloop()

