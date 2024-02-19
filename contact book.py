import tkinter as tk

def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    if name and number:
        contacts[name] = number
        update_contact_list()
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
    else:
        error_label.config(text="Please enter both name and number!")

def update_contact_list():
    contacts_list.delete(0, tk.END)
    for name, number in contacts.items():
        contacts_list.insert(tk.END, f"{name}: {number}")

# Create main window
root = tk.Tk()
root.title("Contact Book")

# Create and add widgets
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Number:").grid(row=1, column=0, sticky="w")
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=2, column=0, columnspan=2, pady=5)

error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=3, column=0, columnspan=2)

contacts_list = tk.Listbox(root)
contacts_list.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Sample contacts dictionary
contacts = {"Rohith": "8897947642"}

# Load initial contacts
update_contact_list()

# Configure grid resizing
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(4, weight=1)

# Start the main event loop
root.mainloop()
