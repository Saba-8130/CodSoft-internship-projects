# PASSWOR GENERATOR USING BY PYTHON GUI.

import tkinter as tk
from tkinter import ttk
import random
import string

#password  characters
def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

#The function to display password on screen.
def display_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            raise ValueError("Length should be a positive integer.")
    except ValueError as e:
        result_label.config(text=f"Error: {e}")
        return

    password = generate_password(password_length)
    result_label.config(text=f"Generated Password: {password}")

#The function to reset password.
def reset():
    length_entry.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x400")

# Create entry place

h1= ttk.Label(root, text="PASSWORD GENERATOR" , font="arial 20 bold")
h1.pack(pady=10)

name=ttk.Label(root , text="Name" ,font="16")
name.pack(pady=10)

name_entry=ttk.Entry(root)
name_entry.pack(pady=10)

      
length_label = ttk.Label(root, text="Enter the desired length:" ,font="16")
length_label.pack(pady=10)

length_entry = ttk.Entry(root)
length_entry.pack(pady=10)

#buttons
generate_button = ttk.Button(root, text="Generate Password", command=display_password)
generate_button.pack(pady=10)

reset_button = ttk.Button(root, text="Reset",command=reset)
reset_button.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()

