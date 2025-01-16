from Users import *

def registerMember(users, lib) -> list:
    k = len(users)    
    n = int(input("How many users: "))

    for i in range(n):
        barcode = k
        name = input(f"(User{k})Enter Name: ")
        user = Member(lib, barcode, name )

        users[barcode, name] = user
        lib.registeredUsers[barcode, name] = user
        k += 1
    return users

def registerLibrarian(users, lib) -> list:
    # k = len(users)    
    # n = int(input("How many users: "))

    # for i in range(n):
    #     barcode = k
    #     name = input(f"(User{k + 1})Enter Name: ")
    #     user = Member(lib, barcode, name )

    #     users[barcode, name] = user
    #     lib.registeredUsers[barcode, name] = user
    #     k += 1
    # return users
    barcode = 0
    name = "Admin"
    user = Librarian(lib, barcode, name)
    users[barcode, name] = user
    lib.registeredUsers[barcode, name] = user