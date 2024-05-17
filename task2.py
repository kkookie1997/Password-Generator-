import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.length_entry = tk.Entry(master, width=10)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.uppercase_var = tk.BooleanVar()
        self.uppercase_check = tk.Checkbutton(master, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_check.grid(row=1, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        self.lowercase_var = tk.BooleanVar()
        self.lowercase_check = tk.Checkbutton(master, text="Include Lowercase Letters", variable=self.lowercase_var)
        self.lowercase_check.grid(row=2, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        self.digits_var = tk.BooleanVar()
        self.digits_check = tk.Checkbutton(master, text="Include Digits", variable=self.digits_var)
        self.digits_check.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        self.special_var = tk.BooleanVar()
        self.special_check = tk.Checkbutton(master, text="Include Special Characters", variable=self.special_var)
        self.special_check.grid(row=4, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.password_label = tk.Label(master, text="")
        self.password_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Please enter a positive integer for password length.")
                return

            characters = ""
            if self.uppercase_var.get():
                characters += string.ascii_uppercase
            if self.lowercase_var.get():
                characters += string.ascii_lowercase
            if self.digits_var.get():
                characters += string.digits
            if self.special_var.get():
                characters += string.punctuation

            if not characters:
                messagebox.showerror("Error", "Please select at least one character type.")
                return

            password = ''.join(random.choice(characters) for _ in range(length))

            self.password_label.config(text="Generated Password: " + password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for password length.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
