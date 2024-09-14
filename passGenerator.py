import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password():
    length = int(length_var.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    char_set = string.ascii_lowercase  # Lowercase letters by default
    
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Password Generator", "Password copied to clipboard!")

# Set up GUI window
window = tk.Tk()
window.title("Password Generator")

# Variables
length_var = tk.StringVar(value="12")
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

# GUI Elements
tk.Label(window, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(window, textvariable=length_var).grid(row=0, column=1, padx=5, pady=5)

tk.Checkbutton(window, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2, padx=5, pady=5)
tk.Checkbutton(window, text="Include Digits", variable=digits_var).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
tk.Checkbutton(window, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

tk.Button(window, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

tk.Label(window, text="Generated Password:").grid(row=5, column=0, padx=5, pady=5)
password_entry = tk.Entry(window, width=30)
password_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI loop
window.mainloop()
