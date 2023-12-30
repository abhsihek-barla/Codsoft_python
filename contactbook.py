import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        # Contact data structure: {name: (phone, email, address)}
        self.contacts = {}

        # UI elements
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)
        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)
        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Packing UI elements
        self.name_label.pack()
        self.name_entry.pack()
        self.phone_label.pack()
        self.phone_entry.pack()
        self.email_label.pack()
        self.email_entry.pack()
        self.address_label.pack()
        self.address_entry.pack()

        self.add_button.pack()
        self.view_button.pack()
        self.search_button.pack()
        self.update_button.pack()
        self.delete_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = (phone, email, address)
            messagebox.showinfo("Success", f"Contact {name} added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contacts_info = "\n".join(f"{name}: {info[0]}" for name, info in self.contacts.items())
            messagebox.showinfo("Contacts", contacts_info)

    def search_contact(self):
        name_or_phone = simpledialog.askstring("Search", "Enter name or phone:")
        if name_or_phone:
            if name_or_phone in self.contacts:
                contact_info = f"{name_or_phone}: {self.contacts[name_or_phone][0]}\n"
                if self.contacts[name_or_phone][1]:
                    contact_info += f"Email: {self.contacts[name_or_phone][1]}\n"
                if self.contacts[name_or_phone][2]:
                    contact_info += f"Address: {self.contacts[name_or_phone][2]}\n"
                messagebox.showinfo("Contact Info", contact_info)
            else:
                messagebox.showinfo("Info", "Contact not found.")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            updated_phone = self.phone_entry.get()
            updated_email = self.email_entry.get()
            updated_address = self.address_entry.get()

            # Update only non-empty fields
            if updated_phone:
                self.contacts[name] = (updated_phone, updated_email, updated_address)
                messagebox.showinfo("Success", f"Contact {name} updated successfully!")
                self.clear_entries()
            else:
                messagebox.showwarning("Error", "Phone is a required field for updating.")
        else:
            messagebox.showinfo("Info", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showinfo("Info", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
