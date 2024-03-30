from ascii import library_logo
import color
from prettytable import PrettyTable

# Book
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = True

# Author
class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

# Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book in self.books:
            print("This book already in libray")
        else:
            self.books.append(book)

    def borrow_book(self, book):
        if book.borrowed:
            book.borrowed = False
            return True
        else:
            return False

    def return_book(self):
        user_choose_book = input("Please enter book name:")
        if len(self.books) != 0:
            for i in range(len(self.books)):
                if user_choose_book == self.books[i].title:
                    if not self.borrow_book(self.books[i]):
                        self.books[i].borrowed = True
                        print("Return book\n")

    def give_book(self):
        user_choose_book = input("Please enter book name:")
        if len(self.books) != 0:
            for i in range(len(self.books)):
                if user_choose_book == self.books[i].title:
                    if self.borrow_book(self.books[i]):
                        print("Give book\n")

    def display_all_book(self):
        if len(self.books) != 0:
            table = PrettyTable()
            table.field_names = ["Book title", "Author", "Genre"]
            for i in range(len(self.books)):
                if self.books[i].borrowed:
                    table.add_row([self.books[i].title, self.books[i].author.name, self.books[i].genre])
            print(f"{table}\n")
        else:
            print("Empty\n")

Xudoberdi_Toxtaboyev = Author("Xudoberdi To'xtaboyev", "o'zbek")
Said_Ahmad = Author("Said Ahmad", "o'zbek")
Gafur_Gilom = Author("G'afur G'ulom", "o'zbek")

Sariq_devni_minib = Book("Sariq devni minib", Xudoberdi_Toxtaboyev, "Fantastika")
Ufq = Book("Ufq", Said_Ahmad, "Badiy")
Shum_bola = Book("Shum bola", Gafur_Gilom, "Badiy")

ziyo = Library()
ziyo.add_book(Sariq_devni_minib)
ziyo.add_book(Ufq)
ziyo.add_book(Shum_bola)

flag = True
while flag:
    print("1)Display all books\n2)Get a book to the Library\n3)Return a book to the Library\n4)Off\n")
    user_choose = input("Please enter operation number:")

    if user_choose in ["1", "2", "3", "4"]:

        if user_choose == "1":
            ziyo.display_all_book()

        elif user_choose == "2":
            ziyo.give_book()

        elif user_choose == "3":
            ziyo.return_book()
        else:
            flag = False
    else:
        print("Choose one\n")
