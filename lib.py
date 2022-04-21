lib = ["book1", "book2", "book3", "book4", "book5"]


def select():
    selection= input("\n \n Which book do you want to select. > ")
    if selection == "book1":
        print(" U took book1!")
    
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
        


bookstore_content = input("Do you want to see the bookstore. > ")
if bookstore_content == "yes":
    print(lib)
    select()
else:
    print("Okay, bye")



any_other_books = input("\n \n Do you want to see any other books. > ")
if any_other_books == "yes":
    print(lib)
    select()
else:
    print("Okay, bye")

print("\n \n Thank you for shopping with us!")
