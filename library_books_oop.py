'''Question:

You are asked to design a simple Library Management System using Python OOP.

Create a class Book with attributes:

title (string)

author (string)

available_copies (int)

It should have methods:

__str__ → returns a nice string representation of the book.

borrow() → reduces available copies by 1 (if available).

return_book() → increases available copies by 1.

Create a class Library that contains:

A list of books.

Methods:

add_book(book) → adds a book to the library.

show_books() → displays all books in the library.

borrow_book(title) → lets a user borrow a book if available.

return_book(title) → lets a user return a borrowed book.

Test your system by:

Creating at least 3 books.

Adding them to the library.

Borrowing and returning some books.

Printing the library status at each step.

👉 Challenge extension (if you want harder):

Add a User class that tracks which books they have borrowed.

Prevent users from borrowing more than 3 books at a time.'''

class Book:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def __str__(self):
        return (f"{self.name} is written by {self.author}\n" 
                f"and there are {self.available_copies} copies available")
    
    def borrow(self):
        if self.available_copies > 1:
            self.available_copies -= 1
            print("{self.title} borrowed successfully")
        else:
            print("No copies of {self.title} available")

    def return_book(self):
        self.available_copies += 1
        print(f"{self.title} returned")

class library:
    def __init__(self):
        self.books = []
    
    def add_books(self, book):
        self.books.append(book)
        print(f"")

    def show_books(self):
        print(self.books)

    def borrow_book(self, title):
        numBook = 0
        for b in self.books:
            numBook += 1
        
