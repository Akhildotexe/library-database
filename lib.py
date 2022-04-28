lib = ["book1", "book2", "book3", "book4", "book5"]
# Simple list database with books in the library.

def select():
# Making a function to select a book from the library.
    selection= input("\n \n Which book do you want to select. > ")

print("You took " + selection)
lib.remove(selection)


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
