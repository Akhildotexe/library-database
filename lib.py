lib = ["book1", "book2", "book3", "book4", "book5"]
# Simple list database with books in the library.

def select():
# Making a function to select a book from the library.
    selection= input("\n \n Which book do you want to select. > ")

   
    print("You took " + selection)
    lib.remove(selection)


""" match selection:
        case "book1":
            print("You took book1")
            lib.remove("book1")
        case "book2":
            print("You took book2")
            lib.remove("book2")
        case "book3":
            print("You took book3")
            lib.remove("book3")
        case "book4":
            print("You took book4")
            lib.remove("book4")
        case "book5":
            print("You took book5")
            lib.remove("book5")
"""

#alternate version:     
"""
    if selection == "book1":
        print(" U took book1!")
        lib.remove("book1")
# When a user selects a book, it will print out the book name then will remove the selected book from the list.

    if selection == "book2":
        print(" U took book2!")
        lib.remove("book2")

    if selection == "book3":
        print(" U took book3!")
        lib.remove("book3")

    if selection == "book4":
        print(" U took book4!")
        lib.remove("book4")

    if selection == "5":
        print(" U took book5!")
        lib.remove("book5")
"""
bookstore_content = input("Do you want to see the bookstore. > ")
if bookstore_content == "yes":
    print(lib)
    select()
# If the user wants to see the bookstore, it will print out the list of books in the library.
else:
    print("Okay, bye")
# Else it will print out "Okay, bruh"

any_other_books = input("\n \n Do you want to see any other books. > ")
if any_other_books == "yes":
    print(lib)
    select()
# If the user wants to see any other books, it will print out the list of books in the library.
else:
    print("Okay, bye")
# Else it will print out "Okay, bye"

print("\n \n Thank you for shopping with us!")
