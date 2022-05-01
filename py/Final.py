import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import jsonpickle
import pickle
from PIL import ImageTk, Image
from tkinter import filedialog
from os.path import exists
import re

"""Book class"""

root = tk.Tk()

class Book:
    def __init__(self, isbn, title, author, purchased, stocked, price, image_path):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.purchased = purchased
        self.stocked = stocked
        self.price = price
        self.image_path = image_path

    def setIsbn(self, isbn):
        self.isbn = isbn

    def setTitle(self, title):
        self.title = title

    def setAuthor(self, author):
        self.author = author

    def setPurchased(self, purchased):
        self.purchased = purchased

    def setStocked(self, stocked):
        self.stocked = stocked

    def setPrice(self, price):
        self.price = price

    def setImagePath(self, image_path):
        self.image_path = image_path

    def getIsbn(self):
        return self.isbn

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getPurchased(self):
        return self.purchased

    def getStocked(self):
        return self.stocked

    def getPrice(self):
        return self.price

    def getImagePath(self):
        return self.image_path

database = []
logEntries = []

file_exists = exists("database.pickle")
if file_exists:
    pickle_off = open("database.pickle","rb")
    database = jsonpickle.decode(pickle.load(pickle_off))
else:
    pickling_on = open("database.pickle","wb")

    mockingbird = Book("1234567890",\
        "To Kill A Mockingbird",\
        "Harper Lee",\
        5,\
        6,\
        13.99,\
        '.\images\mockingbird.jpg')

    database.append(mockingbird)

    pickle.dump(jsonpickle.encode(database), pickling_on)
    pickling_on.close()

def imageFileExplorer(path_label):
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("PNG files","*.png*"), ("all files", "*.*")))
    global file_path
    file_path = filename
    path_label.config(text = file_path)

def addBook():

    """ Creates an add Book button to implement the addBookAction function."""

    global addForm
    addForm = tk.Toplevel(root)
    addForm.title("Add Book to the Database")
    addForm.geometry('500x400')

    isbn = ttk.Label(addForm, text= "ISBN:")
    isbn.grid(row = 0, column = 0)
    title = ttk.Label(addForm, text = "Title:")
    title.grid(row = 1,column = 0)
    author = ttk.Label(addForm, text = "Author:")
    author.grid(row = 2,column = 0)
    purchased = ttk.Label(addForm, text = "# Purchased:")
    purchased.grid(row = 3,column = 0)
    stocked = ttk.Label(addForm, text = "# Stocked:")
    stocked.grid(row = 4,column = 0)
    price = ttk.Label(addForm, text = "Price:")
    price.grid(row = 5, column = 0)
    image_path = ttk.Label(addForm, text = "Cover Art:")
    image_path.grid(row = 6, column = 0)

    isbn_field = ttk.Entry(addForm)
    isbn_field.grid(row = 0,column = 1)
    title_field = ttk.Entry(addForm)
    title_field.grid(row = 1,column = 1)
    author_field = ttk.Entry(addForm)
    author_field.grid(row = 2,column = 1)
    purchased_field = ttk.Entry(addForm)
    purchased_field.grid(row = 3,column = 1)
    stocked_field = ttk.Entry(addForm)
    stocked_field.grid(row = 4, column = 1)
    price_field = ttk.Entry(addForm)
    price_field.grid(row = 5, column = 1)
    
    image_button = tk.Button(addForm, text = "Browse...", command = lambda:imageFileExplorer(image_path))
    image_button.grid(row = 6, column = 1)

    image_path = ttk.Label(addForm, text = "")
    image_path.grid(row = 6, column = 2)

    submit = ttk.Button(addForm, text="Submit", command=lambda:addBookAction(isbn_field.get(), title_field.get(), author_field.get(), purchased_field.get(), stocked_field.get(), price_field.get(), file_path))
    submit.grid(row = 9, column = 0)

#Back end function
def addBookAction(isbn, title, author, purchased, stocked, price, image_path):

    """ Adds a Book to the menu using the user input."""

    # This filters the users' input for illegal input
    authorCheck = re.findall("[^a-zA-Z\s:]", author)
    isbnCheck = re.findall("\D+", isbn)
    purchasedCheck = re.findall("\D+", purchased)
    stockedCheck = re.findall("\D+", stocked)
    try:
        float(price)
        priceCheck = False
    except ValueError:
        priceCheck = True

    if(isbnCheck):
        tkmb.showinfo("ERROR", "ERROR: ISBN must only contain numbers")
        return 0;

    elif(authorCheck):
        tkmb.showinfo("ERROR", "ERROR: Author must only contain alphabetical characters")
        return 0;

    elif(purchasedCheck):
        tkmb.showinfo("ERROR", "ERROR: Purchased must only contain numbers")
        return 0;

    elif(stockedCheck):
        tkmb.showinfo("ERROR", "ERROR: Stocked must only contain numbers")
        return 0;

    elif(priceCheck):
        tkmb.showinfo("ERROR", "ERROR: Price should be a decimal value")
        return 0;
            
    if isbn in database:
        print("ISBN already exists. Please enter a different ISBN.")
        return 0

    else:
        locals()[title] = Book(isbn, title, author, purchased, stocked, price, image_path)
        database.append(locals()[title])
        print("Database updated!")
        addForm.destroy()
        return 0

def findBook(book, index):

    global findForm
    findForm = tk.Toplevel(root)
    findForm.title("Book Information")
    findForm.geometry('500x400')
    
    findBookLabel = tk.Label(findForm)
    findBookLabel.grid(row = 0,column = 0)
    
    isbn = ttk.Label(findForm, text= "ISBN:")
    isbn.grid(row = 0, column = 0)
    isbn = ttk.Entry(findForm)
    isbn.insert(tk.INSERT, book.getIsbn())
    isbn.grid(row = 0, column = 1)

    title = ttk.Label(findForm, text = "Title:")
    title.grid(row = 1,column = 0)
    title = ttk.Entry(findForm)
    title.insert(tk.INSERT, book.getTitle())
    title.grid(row = 1,column = 1)

    author = ttk.Label(findForm, text = "Author:")
    author.grid(row = 2,column = 0)
    author = ttk.Entry(findForm)
    author.insert(tk.INSERT, book.getAuthor())
    author.grid(row = 2,column = 1)

    purchased = ttk.Label(findForm, text = "# Purchased:")
    purchased.grid(row = 3,column = 0)
    purchased = ttk.Entry(findForm)
    purchased.insert(tk.INSERT, book.getPurchased())
    purchased.grid(row = 3,column = 1)

    stocked = ttk.Label(findForm, text = "# Stocked:")
    stocked.grid(row = 4,column = 0)
    stocked = ttk.Entry(findForm)
    stocked.insert(tk.INSERT, book.getStocked())
    stocked.grid(row = 4,column = 1)

    price = ttk.Label(findForm, text = "Price:")
    price.grid(row = 5, column = 0)
    price = ttk.Entry(findForm)
    price.insert(tk.INSERT, book.getPrice())
    price.grid(row = 5, column = 1)

    updateBookButton = ttk.Button(findForm, text="Update Book", command = lambda:updateBookAction(book, isbn.get(), title.get(), author.get(), purchased.get(), stocked.get(), price.get()))
    updateBookButton.grid(row = 6, column = 0)

    delBookButton = ttk.Button(findForm, text="Delete Book", command = lambda:delBookAction(index))
    delBookButton.grid(row = 6, column = 1)

def updateBookAction(book, isbn, title, author, purchased, stocked, price):
    book.setIsbn(isbn)
    book.setTitle(title)
    book.setAuthor(author)
    book.setPurchased(purchased)
    book.setStocked(stocked)
    book.setPrice(price)

def delBookAction(index):

    """ Deletes a Book from the menu."""

    del database[index]
    findForm.destroy()
    return 0

def quit():

    """ Quits the program."""

    pickling_on = open("database.pickle","wb")
    pickle.dump(jsonpickle.encode(database), pickling_on)
    pickling_on.close()
    root.destroy()

if __name__ == '__main__':
    
    root.title("Main View")
    root.geometry('800x300')
    #root.configure(background = "grey");

    menuImageArray = []
    for i in range(0, len(database)):
        menuImageArray.append(ImageTk.PhotoImage(Image.open(database[i].getImagePath()).resize((120, 246))))

    for i in range(0, len(database)):
        menuButton = ttk.Button(root, image = menuImageArray[i], command = lambda:findBook(database[i], i))
        menuButton.grid(row = 0, column = i)
        findBookLabel = tk.Label(root, text=database[i].getTitle())
        findBookLabel.grid(row = 1,column = i)

    menuButtonAdd= ttk.Button(root, text="Add", command = addBook)
    menuButtonAdd.grid(row = 2, column = 0)

    menuButtonQuit = ttk.Button(root, text="Save & Quit", command = quit)
    menuButtonQuit.grid(row = 2, column = 1)

    root.mainloop()
