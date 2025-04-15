import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.configure(bg="#f4f4f4")

# Dummy credentials (you can replace these with a database check)
USER_CREDENTIALS = {"admin": "1234", "user": "password"}

# Function to check login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login Success", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# UI Elements
tk.Label(root, text="Login", font=("Arial", 20, "bold"), bg="#f4f4f4").pack(pady=20)

tk.Label(root, text="Username:", font=("Arial", 12), bg="#f4f4f4").pack()
entry_username = tk.Entry(root, font=("Arial", 12))
entry_username.pack(pady=5)

tk.Label(root, text="Password:", font=("Arial", 12), bg="#f4f4f4").pack()
entry_password = tk.Entry(root, font=("Arial", 12), show="*")  # Mask password input
entry_password.pack(pady=5)

# Login Button
tk.Button(root, text="Login", font=("Arial", 12, "bold"), bg="green", fg="white", command=login).pack(pady=20)

# Run Tkinter event loop
root.mainloop()
