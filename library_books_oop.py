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
        return f"{self.title} by {self.author} - {self.available_copies} copies left"
    
    def borrow(self):
        if self.available_copies > 0: 
            self.available_copies -= 1
            print(f"{self.title} by {self.author} borrowed")
        else:
            print("No more copies left")

    def return_book(self):
        self.available_copies += 1
        print(f"{self.title} by {self.author} returned")

class Library:
    def __init__(self):
        self.books = []

    def add_books(self,book):
        self.books.append(book)
        print(f"{book.title} added")

    def show_books(self):
        if not self.books:
            print("No books in the library")
        else:
            print("Available Books:")
            for book in self.books:
                print(book)
            print("-" * 40)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow()
                return
            
        print(f"{title} not found in the library")

    def return_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        
        print(f"{title} is not in the library")


library = Library()
library.show_books()

book1 = Book("Sejarah Melayu (Malay Annals)", "Tun Seri Lanang", 3)
book2 = Book("Bustan al-Salatin", "Nuruddin al-Raniri", 4)
book3 = Book("Hidayat al-Salikin", "Abd al-Samad al-Palimbani", 2)

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

library.show_books()

library.borrow_book("Hidayat al-Salikin")
library.borrow_book("Hidayat al-Salikin")
library.borrow_book("Hidayat al-Salikin")

library.show_books()

library.return_book("Hidayat al-Salikin")
library.return_book("Hidayat al-Salikin")
library.return_book("Hidayat al-Salikin")

library.show_books()