import tkinter as tk
import sqlite3

class UserInterface:
    def __init__(self, master):
        self.master = master
        self.create_widgets()
        self.connect_to_database()

    def connect_to_database(self):
        self.conn = sqlite3.connect('DL.db')
        self.c = self.conn.cursor()

    def create_widgets(self):
        self.label_username = tk.Label(self.master, text="Username:")
        self.label_username.pack()

        self.entry_username = tk.Entry(self.master)
        self.entry_username.pack()

        self.label_password = tk.Label(self.master, text="Password:")
        self.label_password.pack()

        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack()

        self.button_save = tk.Button(self.master, text="Save", command=self.save_to_database)
        self.button_save.pack()

    def save_to_database(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Insert data into the database table
        self.c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()

        # Clear the input fields after saving
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_username.focus()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("User Interface")
    root.geometry("300x200")

    app = UserInterface(root)
    root.mainloop()
