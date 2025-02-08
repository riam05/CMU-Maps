import tkinter as tk
from tkinter import ttk

TK_SILENCE_DEPRECATION=1
# Sample list of rooms
rooms = ["4301", "4303", "4302", "4305", "4307", "4309", "4310", "4352", "4311", "4313", "4314", "4315", "4317", "4319", "4318", "4322", "4354", "4321", "4323", "4325", "4326", "4356", "4342", "4338", "4340", "4342", "4432", "4435", "4436", "4501", "4503", "4504", "4505", "4602", "4604", "4605", "4606", "4607", "4608", "4609", "4610", "4612", "4611", "4614", "4616", "4701", "4701A", "4702", "4703"]

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
