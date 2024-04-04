import tkinter as tk
from tkinter import messagebox

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Perform validation checks
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        # You can add more validation checks here (e.g., checking username and password against a database)

        # If all validations pass, show success message
        messagebox.showinfo("Success", "Login successful!")

        # Clear the entry fields after successful login
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def create_widgets(self):
        username_label = tk.Label(self.master, text="Username:", font=("Times", 24)).place(x=400, y=295)
        #username_label.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

        self.username_entry = tk.Entry(self.master, font=("Times", 24),width=25)
        self.username_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        password_label = tk.Label(self.master, text="Password:", font=("Times", 24)).place(x=400, y=375)
        #password_label.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

        self.password_entry = tk.Entry(self.master, show="*", font=("Times", 24),width=25)
        self.password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        save_button = tk.Button(self.master, text="Save",width=6, height=1, background="#FFD39B", font=("Times", 30)).place(x=692,y=480)
        login_button = tk.Button(self.master, text="Login", command=self.validate_login, width=10, height=1, background="#FFD39B", font=("Times", 30)).place(x=650,y=600)
        #login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Login")
    root.geometry("400x300")

    login_page = LoginPage(root)

    root.mainloop()
