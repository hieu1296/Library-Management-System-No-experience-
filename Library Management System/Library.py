import collections
from Users import *
from Book import *


class Library:
    def __init__(self) -> None:
        self.userID = 0
        self.registeredUsers = {}
        self.libraryStorage =  {}
        self.catTitles = collections.defaultdict(list)
        self.catAuthors = collections.defaultdict(list)
        self.catDate = collections.defaultdict(list)
        self.id = 0

    def addBook(self,title, author, status, PublicationDate)-> None:
        book = Book(id = self.id, title=title, author = author, status=status, PublicationDate=PublicationDate)
        self.catTitles[title].append(book)
        self.catAuthors[author].append(book)
        self.catDate[PublicationDate].append(book)
        self.libraryStorage[self.id] = book
        self.id += 1

    def print_book_data(self, book):
        print(book.id)
        print(book.title)
        print(book.author)
        print(book.status)
        print(book.PublicationDate)
        print("------------------------------------------------")

    def displayTitle(self, title) -> None:
        for book in self.catTitles[title]:
            self.print_book_data(book)
        return None
    
    def displayAuthor(self, author) -> None:
        for book in self.catAuthors[author]:
            self.print_book_data(book)
        return None
    
    def displayDate(self, date) -> None:
        for book in self.catDate[date]:
            self.print_book_data(book)
        return None










    # def addBook(self, title, author):
    #     book = Book(title, author=author, id = self.id)
    #     self.books[title].append(book)
    #     self.available_books[title].append(book)
    #     self.id += 1
    
    # def borrowbook(self, title):
    #     if self.books[title] == None:return None
    #     book = self.books[title].popleft()
    #     book.updatestatus("Borrowed")
    #     self.borrwed_books[(title, book.id)] = book
    
    # def returnbook(self, title, id):
    #     book = self.borrwed_books[(title, id)]
    #     del self.borrwed_books[(title, id)]
    #     self.books[title].append(book)

    # def bookReservation(self, title):
    #     if self.books[title] == None:return None



