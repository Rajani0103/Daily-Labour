import tkinter as tk
import sqlite3
from tkinter import *
from PIL import ImageTk

class DisplayDataApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Display Data")
        self.create_widgets()
        self.connect_to_database()
        self.fetch_and_display_data()

    def connect_to_database(self):
        self.conn = sqlite3.connect('DL.db')  # Replace 'your_database.db' with your database file
        self.c = self.conn.cursor()

    def fetch_and_display_data(self):
        self.c.execute("SELECT * FROM driver")  # Replace 'users' with your table name
        data = self.c.fetchall()
        
        for row_index, row in enumerate(data):
            for col_index, value in enumerate(row):
                label = tk.Label(self.master, text=value)
                label.grid(row=row_index, column=col_index)

    def create_widgets(self):
        # Add any additional widgets if needed
        #button = tk.Button(root, text="Retrieve Data", command=DisplayDataApp)
        #button.pack()

        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = DisplayDataApp(root)
    root.mainloop()
