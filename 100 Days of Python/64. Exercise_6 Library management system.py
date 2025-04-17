# Two Compulsory variables - no. of books, books (list)
# Method which checks if no. of books is equal to len(books)

class Library:
    def __init__(self):
        self.number_of_books = 2
        self.books = ["Harry Potter", "The Avengers"]
        
    def check_stock(self):
        if len(self.books) == self.number_of_books:
            print("Stock System At Optimal")
            
    def add_book(self):
        book_name = input("Enter Book Name: ")
        self.books.append(book_name)
        self.number_of_books += 1
        
    def remove_book(self):
        book_name = input("Enter Book To Remove: ")
        self.books.remove(book_name)
        self.number_of_books -= 1
        
    def Show_books(self):
        for index, items in enumerate(self.books, start=0):
            print(f"{index}. {items}")

Library1 = Library()
Library1.check_stock()
Library1.add_book()
Library1.remove_book()
Library1.Show_books()