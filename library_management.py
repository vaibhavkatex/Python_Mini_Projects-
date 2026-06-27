# Library Management System

books = {
    "101": {"title": "Atomic Habits", "author": "James Clear", "status": "Available"},
    "102": {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "status": "Available"},
    "103": {"title": "Ikigai", "author": "Hector Garcia", "status": "Available"},
    "104": {"title": "Deep Work", "author": "Cal Newport", "status": "Available"},
    "105": {"title": "The Psychology of Money", "author": "Morgan Housel", "status": "Available"}
}


def add_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:
        print("Book already exists!")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    books[isbn] = {
        "title": title,
        "author": author,
        "status": "Available"
    }

    print("Book Added Successfully!")


def issue_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:

        if books[isbn]["status"] == "Available":
            books[isbn]["status"] = "Issued"
            print("Book Issued Successfully!")

        else:
            print("Book Already Issued!")

    else:
        print("Book Not Found!")


def return_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:

        if books[isbn]["status"] == "Issued":
            books[isbn]["status"] = "Available"
            print("Book Returned Successfully!")

        else:
            print("Book is already available!")

    else:
        print("Book Not Found!")


def search_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:

        print("Title :", books[isbn]["title"])
        print("Author :", books[isbn]["author"])
        print("Status :", books[isbn]["status"])

    else:
        print("Book Not Found!")


def view_books():

    print("\n===== ALL BOOKS =====")

    for isbn, book in books.items():

        print("-------------------")
        print("ISBN :", isbn)
        print("Title :", book["title"])
        print("Author :", book["author"])
        print("Status :", book["status"])


while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View All Books")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        search_book()

    elif choice =="5":
        view_books()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")