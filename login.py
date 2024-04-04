from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('DL.db')
print("Opened database successfully")
c = conn.cursor()

ws = Tk()
ws.geometry('5000x5000')
ws.title('LOGIN')
ws['bg'] = '#5d8a82'

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.uname_label = Label(ws, text="Username", font=(23))
        self.uname_label.place(x=500, y=150)
        self.e1 = Entry(width=25, font=(20))
        self.e1.place(x=600, y=150)

        self.password_label = Label(ws, text="Password", font=(23))
        self.password_label.place(x=500, y=200)
        self.e2 = Entry(show='*', width=25, font=(20))
        self.e2.place(x=600, y=200)

        Button(ws, text="Save", background="lightgreen", command=self.insert_data, width=15, height=2, font=(23)).place(x=590, y=300)
        Button(ws, text="LOGIN", background="lightgreen", command=self.provider_needer, width=25, height=2,font=(20)).place(x=550, y=400)
        Button(ws, text="back", background="lightblue", command=self.main, width=9, height=1, font=(20)).place(x=620,y=650)

    def insert_data(self):
        Username = self.e1.get()
        Password = self.e2.get()
        insert_query = "INSERT INTO `login`(`Username`,`Password`)VALUES(?,?)"
        vals = (Username, Password)
        c.execute(insert_query, vals)
        conn.commit()

    def provider_needer(self):
        ws.destroy()
        import provider_needer

    def main(self):
        ws.destroy()
        import main


login_page = LoginPage(ws)
ws.mainloop()
