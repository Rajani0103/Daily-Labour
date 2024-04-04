from tkinter import *
from PIL import ImageTk

ws = Tk()

ws.geometry('10000x10000')
ws.title('confirm')
ws['bg']='Cadetblue4'



Label(ws,text="YOU HAVE CONFIRMED",font=("Comic Sans MS",25,"bold"),background='pink2').place(x=520,y=500)
Label(ws,text="THANK YOU!!",font=("Comic Sans MS", 15,"bold"),background='pink2').place(x=650,y=550)

ws.mainloop()
