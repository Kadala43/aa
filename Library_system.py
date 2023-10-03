'''
GROUP 7
CSC/20U/4078 , CSC/20U/3988, CSC/20U/4079, CSC/20U/4032, CSC/20U/4005, CSC/20U/18U/1008, CSC/20U/4100, CSC/20U/4088
'''
import tkinter as tk
from tkinter import messagebox
class LibraryItem:
    def __init__(self, title, location,item_type):
        # Initialize the item with a title, location, and status
        self.item_type = item_type
        self.title = title
        self.location = location
        self.status = "Available"

    def borrow(self):
        # Change the status to "Borrowed" when the item is borrowed
        self.status = "Borrowed"

    def return_item(self):
        # Change the status back to "Available" when the item is returned
        self.status = "Available"

    def display_details(self):
        # Display the details of the library item
        return f"Title: {self.title}\nLocation: {self.location}\nStatus: {self.status}\nItem Type:{self.item_type}"

#Create a class for books that inherits from LibraryItemm
class Book(LibraryItem):
    def __init__(self, title, location, author,item_type):
        # Initialize a Book with a title, location, and author
        super().__init__(title, location,item_type)
        self.author = author

    def display_details(self):
        # Display book details
        return super().display_details() + f"\nAuthor: {self.author}"

# Create a class for DVDs inheriting from LibraryItem.
class DVD(LibraryItem):
    def __init__(self, title, location, director,item_type):
        # Initialize a DVD with a title, location, and director
        super().__init__(title, location,item_type)
        self.director = director

    def display_details(self):
        # Display DVD details
        return super().display_details() + f"\nDirector: {self.director}"

#Create the main Library class to manage items.
class Library:


    def __init__(self):
        # Initialize an empty list to store library items.
        self.items = []

    def add_item(self, item):
        # Add a new item to the library.
        self.items.append(item)

    def borrow_item(self, title, item_type):
        # Borrow an item by changing its status
        for item in self.items:
            if item.title == title and item.status == "Available" and item.item_type == item_type:
                item.borrow()
                return f"{title} has been borrowed."
        return f"{title} is not available for borrowing."

    def return_item(self, title,item_type):
        # Return a borrowed item by changing its status
        for item in self.items:
            if item.title == title and item.status == "Borrowed" and item.item_type == item_type:
                item.return_item()
                return f"{title} has been returned."
        return f"{title} cannot be returned."

    
    def list_all_items(self):
        # Return a list of details for all library items
        return [item.display_details()for item in self.items]
    

    def delete_item(self, title):
        # Delete an item from the library based on its title
        for item in self.items:
            if item.title == title:
                self.items.remove(item)
                return f"{title} has been deleted from the library."
        return f"{title} was not found in the library."

    
#create a gui using tkinter
class LibraryApp:
    def __init__(self, root,):
        self.root = root
        root.configure(bg="light blue")

        self.root.title("Library System",)
        self.frame = tk.Frame(root, ) 
        self.frame.pack(padx=280, pady=170)
      
        # Create a library instance to manage items
        self.library = Library()

        # Create the GUI elements
        self.create_gui()
    

    def delete_item(self):
        title = self.titleEntry.get()
        if title:
            message = self.library.delete_item(title)
            self.resultLabel.config(text=message)
        else:
            self.resultLabel.config(text="Please enter a title.")
   

    def reset_entry(self):
        self.titleEntry.delete(0,tk.END)
        self.locationEntry.delete(0,tk.END)
        self.authorDirectorEntry.delete(0,tk.END)

    def create_gui(self):
        # Create labels, entry fields, buttons, and result labels.
        self.titleLabel = tk.Label(self.root, text="Title",bg="light blue")
        self.titleLabel.place(x=55,y=25)
        self.titleEntry = tk.Entry(self.root)
        self.titleEntry.place(x=5,y=50)

        self.locationLabel = tk.Label(self.root, text="Location",bg="light blue")
        self.locationLabel.place(x=240,y=25)

        self.locationEntry = tk.Entry(self.root)
        self.locationEntry.place(x=200,y=50)

        self.authorDirectorLabel = tk.Label(self.root, text="Author/Director",bg="light blue")
        self.authorDirectorLabel.place(x=420,y=25)

        self.authorDirectorEntry = tk.Entry(self.root,)
        self.authorDirectorEntry.place(x=400,y=50)

        self.itemTypeLabel = tk.Label(self.root, text="Item Type",bg="light blue")
        self.itemTypeLabel.place(x=245,y=100)

        self.itemTypeVar = tk.StringVar()
        self.itemTypeVar.set("Book")

        self.itemTypeOption = tk.OptionMenu(self.root, self.itemTypeVar, "Book", "DVD")
        self.itemTypeOption.place(x=240,y=130)

        self.addButton = tk.Button(self.root, text="Add Item", command=self.add_item,bg="#27cbe8")
        self.addButton.place(x=60,y=200)

        self.borrowButton = tk.Button(self.root, text="Borrow Item", command=self.borrow_item,bg="#27cbe8")
        self.borrowButton.place(x=170,y=200)

        self.returnButton = tk.Button(self.root, text="Return Item", command=self.return_item,bg="#27cbe8")
        self.returnButton.place(x=300,y=200)

        self.listButton = tk.Button(self.root, text="List All Items", command=self.list_items,bg="#27cbe8")
        self.listButton.place(x=420,y=200)

        self.delete_itemButton= tk.Button(self.root,text="DELETE ITEM",font="BOLD",command=self.delete_item).place(x=215,y=290)
        self.resultLabel = tk.Label(self.root, text="",bg="light blue")
        self.resultLabel.pack()
        self.resetButton=tk.Button(self.root,text="RESET",font="BOLD",command=self.reset_entry).place(x=240,y=250)


        #Adding items to the library
    def add_item(self):
        title = self.titleEntry.get()
        location = self.locationEntry.get()
        author_director = self.authorDirectorEntry.get()
        item_type = self.itemTypeVar.get()

        if title and location and author_director:
            if item_type == "Book":
                item = Book(title, location, author_director,item_type)
            elif item_type == "DVD":
                item = DVD(title, location, author_director,item_type)
            else:
                messagebox.showerror("Error", "Invalid item type.")
                return

            self.library.add_item(item)
            self.resultLabel.config(text="Item added successfully.")
        else:
            self.resultLabel.config(text="Please fill in all fields.")

                #borrowing items from the library
    def borrow_item(self):
        title = self.titleEntry.get()
        item_type = self.itemTypeVar.get()

        if title:
            message = self.library.borrow_item(title,item_type)
            self.resultLabel.config(text=message)
        else:
            self.resultLabel.config(text="Please enter a title.")
         
            #returning items back to the library
    def return_item(self):
        title = self.titleEntry.get()
        item_type = self.itemTypeVar.get()
        if title:
            message = self.library.return_item(title,item_type)
            self.resultLabel.config(text=message)
        else:
            self.resultLabel.config(text="Please enter a title.")
           
            #listing all the items in the library
    def list_items(self):
        items = self.library.list_all_items()
        if items:
            item_details = "\n\n".join(items)
        else:
            item_details = "No items in the library."
        messagebox.showinfo("Library Items", item_details,)

      
root = tk.Tk()

app = LibraryApp(root)

root.mainloop()
