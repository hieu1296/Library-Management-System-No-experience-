from Library import *
from Book import *

class User:
    def __init__(self, lib ,barcode:str = None, name:str = None):
        self.barcode = barcode
        self.name = name
        self.lib = lib
        # DOB, CITIES, ETC, IDK ABOUT LIBRARY SYSTEMS IRL

    def checkout(self):
        pass

    def borrow_book(self, book): # Assume Librarian and Member can borrow books in different cases
        pass

    def renew(self):
        pass

    def return_book(self, book):
        book.status = "Available"

    # 0 -> title, 1 -> author, 2 -> Date
    def search_catalog_By_Request(self , title = None, author = None, Date= None) -> None: 
        
        if title:
            self.lib.displayTitle(title)
        elif author:
            self.lib.displayAuthor(author)
        elif Date:
            self.lib.displayDate(Date)
        else:
            print("You Entered Nothing adios !")


class Librarian(User):
    def __init__(self, lib, barcode, name):
        super().__init__(lib, barcode, name)
        self.booksborrowed = set()


    def addBook(self,title, author, status, publicationDate):
        self.lib.addBook(title, author, status, publicationDate)

    def return_book(self, book):
        super().return_book(book)
        self.booksborrowed.remove(book)

    def removeUser(self, barcode, name):
        self.lib.registeredUsers[barcode,name].updateRegisteredStatus(False) 

        if (barcode, name) in self.lib.registeredUsers: 
            # del self.lib.registeredUsers[(barcode, name)] # should i delete it from registeredUsers ?
            self.lib.registeredUsers[barcode,name].updateRegisteredStatus(False) 
            print(f"User {name} removed successfully.")
        else:
            print(f"User {name} not found.")

class Member(User):
    def __init__(self, lib, barcode, name):
        super().__init__(lib, barcode, name)
        self.borrowed_books = {}
        self.registered = True

    # def updateBooksBorrowed(self):
    #     self.booksborrowed += 1

    def updateRegisteredStatus(self, status):
        self.registered = status

    def borrow_book(self,id, book):
        super().borrow_book(book)
        if len(self.borrowed_books) >= 3:
            print("Vuot gioi han roi")
            return None
        if book.status == "Available":
            book.updatestatus("Borrowed")
            self.borrowed_books[id] = book
        else:
            print(f"Book {book.title} is not available for bosrrowing.")

    def return_book(self, id, book):
        super().return_book(book)
        
        # self.booksborrowed.remove(book)
    
        if id in self.borrowed_books:
            self.borrowed_books[id].updatestatus("Available")
            # self.borrowed_books.remove(book)
            del self.borrowed_books[id]
        else:
            print(f"Book {book.title} was not borrowed by {self.name}.")
