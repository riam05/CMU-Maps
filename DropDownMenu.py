import tkinter as tk
from tkinter import ttk

TK_SILENCE_DEPRECATION=1
# Sample list of rooms
rooms = ["4301", "4302", "4310", "4315", "4320"]

def on_select(event):
    selected_room = dropdown_var.get()
    print(f"Selected starting room: {selected_room}")

# Create window
root = tk.Tk()
root.title("Wean Hall Path Finder")

# Dropdown menu
dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=rooms)
dropdown.pack(pady=20)
dropdown.bind("<<ComboboxSelected>>", on_select)

# Run GUI
root.mainloop()
