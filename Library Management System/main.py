from Library import *
from Users import *
from Book import *
from Register import *
import datetime
import collections


#keep tracking of time

# test1 = datetime.datetime.now()

# print(type(test1))


if __name__ == "__main__":


    # Init
    users = {}
    lib = Library()
    registerLibrarian(users, lib)
    Admin = users[(0, 'Admin')] if (0, 'Admin') in users else None

    #Implementation
    registerMember(users, lib)
    print(lib.registeredUsers)

    # Remove user example
    if (1, 'dat') in lib.registeredUsers:
        Admin.removeUser(1, 'dat')
        print(lib.registeredUsers[(1, 'dat')].registered)
    else:
        print("User 'dat' not found in registered users.")



    # Admin.addBook("datBook", "datlo","Available", "28/10")
    # Admin.addBook("datgiga", "thuangigachad","Available", "13/10")
    # Admin.addBook("datkcBook", "datlo","Available", "28/10")

    Admin.addBook("datBook", "datlo","Available", "28/10")
    Admin.addBook("datgiga", "thuangigachad","Available", "13/10")
    Admin.addBook("datkcBook", "datlo","Available", "28/10")
    Admin.addBook("datmegenshin", "datlo","Available", "28/10")

    UserSample = lib.registeredUsers[(1, 'dat')] if (1, 'dat') in lib.registeredUsers else None
    if UserSample:
        for book in lib.catAuthors['datlo']: # borrow by author
            print(book.title)
            print(book.id)
            print(book.status)
            UserSample.borrow_book(book.id, book)

    if UserSample:
        for id, book in UserSample.borrowed_books.items(): # borrow by author
            print(book.title)
            print(book.id)
            print(book.status)


    # Admin.search_catalog_By_Request( author="datlo")
