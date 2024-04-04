from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

def login():
    ws.destroy()
    import login

def register():
    ws.destroy()
    import register

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.load_background()
        self.create_widgets()

    def load_background(self):
        image = Image.open('start.png')  # Replace 'start.png' with your image file
        self.bg_img = ImageTk.PhotoImage(image)

    def login(self):
        # Add your login functionality here
        print("Login button clicked")

    def register(self):
        # Add your register functionality here
        print("Register button clicked")

    def create_widgets(self):
        background_label = tk.Label(self.master, image=self.bg_img)
        background_label.place(relwidth=1, relheight=1)  # Stretch the background image to cover the entire window

        login_button = tk.Button(self.master, text="Login", command=login, width=12, height=2, bg="#FFD39B", font=("Times", 30))
        login_button.place(x=300, y=550)

        register_button = tk.Button(self.master, text="Register", command=register, width=12, height=2, bg="#FFD39B", font=("Times",30))
        register_button.place(x=970, y=550)

if __name__ == "__main__":
    ws = Tk()
    ws.geometry('5000x5000')
    ws.title('PROVIDER OR NEEDER')
    ws['bg'] = '#5d8a82'
    
    login_page = LoginPage(ws)
    ws.mainloop()
