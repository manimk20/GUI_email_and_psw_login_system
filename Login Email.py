import re
import tkinter as tk
from tkinter import messagebox
def validate_login():
    email = email_entry.get().strip()
    password = password_entry.get()

    if re.search(
            r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
            email):
        # Password validation (must be between 8 and 20 characters, alphanumeric)
        if re.search(r"^[a-zA-Z0-9@#$%^&+=]{8,20}\w$", password):
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid password! Must be 8-20 characters, alphanumeric, Special Character.")
    else:
        messagebox.showerror("Error", "Invalid email format!")

root = tk.Tk()
root.title("Login System")

email_label = tk.Label(root, text="Email id: ")
email_label.grid(row=0, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Password: ")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=2, column=1)

root.mainloop()


