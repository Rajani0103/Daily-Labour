from tkinter import *
from PIL import ImageTk

ws = Tk()

ws.geometry('10000x10000')
ws.title('thankyou')
ws['bg']='Cadetblue4'

Label(ws,text="DAILY LABOUR",font=("Comic Sans MS",24,"bold")).place(x=620,y=200)
Label(ws,text="THANK YOU!!",font=("Comic Sans MS",22,"bold")).place(x=640,y=500)
Label(ws,text="FOR CHOOSING US",font=("Comic Sans MS",20,"bold")).place(x=600,y=580)

ws.mainloop()
